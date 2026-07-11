"""Forward-only scored-record persistence for scripted dialogue transcripts."""

import pytest

from walkworthy.clients import MockModelClient
from walkworthy.executors import execute_item
from walkworthy.judges import MockJudge
from walkworthy.loader import load_design
from walkworthy.manifest import FIXED_PERMUTATION_SEEDS
from walkworthy.run import score_item


@pytest.mark.parametrize("design", ["02-twomasters", "07-seventyseven"])
def test_score_item_persists_every_scripted_turn_and_legacy_alias(
        benchmark_root, design):
    item = load_design(design, benchmark_root, include_exemplars=False)[0]
    execution = execute_item(
        item,
        MockModelClient("mock-transcript", seed=2),
        FIXED_PERMUTATION_SEEDS,
    )
    administration = next(a for a in execution.administrations if a.label == "main")
    expected_turns = [
        {
            "index": turn.index,
            "user_text": turn.user_text,
            "response": turn.response,
            "branch_state": turn.branch_state,
            "refused_hint": turn.refused_hint,
        }
        for turn in administration.turns
    ]

    record = score_item(
        item,
        execution,
        [
            MockJudge("mock-judge-a", family="anthropic"),
            MockJudge("mock-judge-b", family="openai"),
        ],
    )
    serialized = next(a for a in record["administrations"] if a["label"] == "main")

    assert {key: serialized[key] for key in
            ("label", "kind", "response", "n_turns", "terminal")} == {
        "label": administration.label,
        "kind": administration.kind,
        "response": administration.turns[0].response,
        "n_turns": len(administration.turns),
        "terminal": administration.terminal_response,
    }
    assert serialized["system"] == administration.system
    assert serialized["turns"] == expected_turns
    assert serialized["response"] == serialized["turns"][0]["response"]
    assert serialized["terminal_user_text"] == administration.terminal_user_text
    assert serialized["terminal_response"] == administration.terminal_response
    assert serialized["terminal"] == serialized["terminal_response"]

    if design == "07-seventyseven":
        assert serialized["terminal_user_text"]
        assert serialized["terminal_response"]
