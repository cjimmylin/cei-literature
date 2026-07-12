from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest


BANK = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BANK))

import selfcheck  # noqa: E402
from lib.blocks import build_deep_structures  # noqa: E402


def item(index: int, split: str) -> dict:
    return {
        "id": f"CROSSROADS-{index:04d}",
        "split": split,
        "canary": (
            f"10CB3-01-{index:08x}-{index % 65536:04x}-"
            f"4{index % 4096:03x}-8{index % 4096:03x}-{index:012x}"
        ),
    }


def test_exact_bank_counts_are_fail_loud():
    private = [item(i, "private") for i in range(1, 601)]
    public = [item(i, "public") for i in range(601, 631)]
    assert selfcheck.check_counts(private, public) == "630 episodes (600 private + 30 public)"
    with pytest.raises(AssertionError, match="private episode count"):
        selfcheck.check_counts(private[:-1], public)


def test_canary_registry_requires_630_unique_item_bound_mappings(tmp_path):
    episodes = [item(i, "private" if i <= 600 else "public") for i in range(1, 631)]
    registry = tmp_path / "canary_registry.txt"
    registry.write_text("".join(f"{row['canary']}\t{row['id']}\n" for row in episodes))
    result = selfcheck.check_canaries(episodes, registry)
    assert result == "630 unique registered canaries"
    episodes[-1]["canary"] = episodes[0]["canary"]
    with pytest.raises(AssertionError, match="unique"):
        selfcheck.check_canaries(episodes, registry)


def test_judge_seed_map_and_hardness_log_have_exact_complete_accounting(tmp_path):
    episodes = [item(i, "private" if i <= 600 else "public") for i in range(1, 631)]
    judge_map = {
        f"JSEED-{i:08x}-{i % 65536:04x}-4{i % 4096:03x}-8{i % 4096:03x}-{i:012x}": row["id"]
        for i, row in enumerate(episodes, 1)
    }
    assert selfcheck.check_judge_seed_map(episodes, judge_map) == (
        "630 private authoring JSEED mappings (zero pre-issued JCASE tokens)"
    )
    hardness = [
        {"candidate_id": row["id"], "decision": "accepted", "reasons": []}
        for row in episodes
    ] + [
        {"candidate_id": f"REJECTED-{i:04d}", "decision": "rejected",
         "reasons": ["no real cost"]}
        for i in range(1, 41)
    ]
    assert selfcheck.check_hardness(episodes, hardness) == "670 hardness decisions (630 accepted + 40 rejected)"
    hardness.pop()
    with pytest.raises(AssertionError, match="rejected hardness"):
        selfcheck.check_hardness(episodes, hardness)


def test_judge_roster_assets_are_schema_valid_and_explicitly_mock_only():
    assert selfcheck.check_judge_roster_assets(BANK) == (
        "hash-frozen mock JUDGE roster validates; actual roster remains external"
    )


def test_public_redaction_rejects_keys_clause_signs_and_private_logic():
    clean = [{
        "id": "CROSSROADS-0001", "split": "public",
        "multiturn_script": {f"stage_{i}": f"visible phase {i}" for i in range(1, 5)},
        "tools": [], "affordances": [{}, {}, {}], "visible_consequences": [],
    }]
    assert selfcheck.check_public_redaction(clean) == "public YAML is key-redacted"
    clean[0]["path_keys"] = {"p0": {"C1": 1}}
    with pytest.raises(AssertionError, match="redaction"):
        selfcheck.check_public_redaction(clean)
    clean[0].pop("path_keys")
    clean[0]["failure_modes"] = ["hidden harsh pole"]
    with pytest.raises(AssertionError, match="redaction"):
        selfcheck.check_public_redaction(clean)


def test_stated_pairs_are_60_unique_matches_with_balanced_order_schedule():
    episodes = [item(i, "private" if i <= 600 else "public") for i in range(1, 631)]
    pairs = [
        {
            "pair_id": f"STATED-{i:04d}",
            "enacted_item_id": episodes[i]["id"],
            "order": "stated_first" if i < 30 else "enacted_first",
            "stated_item": {"vignette": f"Matched situation {i}", "affordances": [1, 2, 3]},
        }
        for i in range(60)
    ]
    assert selfcheck.check_stated_pairs(episodes, pairs) == (
        "60 unique stated/enacted pairs (30 per order)"
    )
    pairs[-1]["enacted_item_id"] = pairs[0]["enacted_item_id"]
    with pytest.raises(AssertionError, match="unique enacted"):
        selfcheck.check_stated_pairs(episodes, pairs)


def test_scope_scan_catches_sibling_bench_reference_without_literal_in_source(tmp_path):
    target = tmp_path / "README.md"
    target.write_text("See " + "CHARI" + "TROC for implementation details.\n")
    with pytest.raises(AssertionError, match="scope"):
        selfcheck.check_scope_and_citations(tmp_path)


def test_ground_truth_semantics_replay_paths_reactions_evasion_and_twin_poles():
    clauses = ["C1", "C2", "C3", "C4"]
    vectors = (
        (1, 1, -1, -1), (1, -1, -1, 1),
        (-1, 1, 1, -1), (-1, -1, 1, 1),
    )
    affordances = [
        {"tool": "workspace.send", "target": f"target-{i}",
         "operation": "commit", "arguments": {"index": i},
         "description": f"Action {i}"}
        for i in range(4)
    ]
    episode = {"id": "CROSSROADS-0001", "affordances": affordances}
    hidden = {
        "clauses": clauses,
        "path_specs": [
            {"path_id": f"p{i}", **{key: affordance[key] for key in (
                "tool", "target", "operation", "arguments"
            )}}
            for i, affordance in enumerate(affordances)
        ],
        "path_keys": {
            f"p{i}": dict(zip(clauses, vector))
            for i, vector in enumerate(vectors)
        },
        "reaction_table": {
            **{f"p{i}": {"turns": ["a", "b", "c"]} for i in range(4)},
            "evasion": {"turns": ["a", "b", "c"]},
        },
        "evasion_key": {clause: -1 for clause in clauses},
        "evasion_paths": [],
        "fork_open_turn": 3,
        "fork_window_turns": 3,
    }
    assert selfcheck.check_ground_truth_semantics([episode], {episode["id"]: hidden}) == (
        "semantic path/reaction/evasion/twin-pole contracts pass"
    )
    hidden["reaction_table"]["p0"]["turns"] = ["a", "b"]
    with pytest.raises(AssertionError, match="3..8"):
        selfcheck.check_ground_truth_semantics([episode], {episode["id"]: hidden})


def test_actual_deep_structure_design_has_rank_fifteen_and_twin_balance():
    report = selfcheck.check_design_rank(build_deep_structures())
    assert report["rank"] == 15
    assert report["minimum_pair_coverage"] == 2
