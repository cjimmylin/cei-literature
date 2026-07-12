from __future__ import annotations

from collections import Counter, defaultdict
from copy import deepcopy
import inspect
import re

from generator import build_bank
from lib.scenarios import observable_effect
from lib.sign_leak import audit
from lib.split_hygiene import future_visible_surface
import json


def test_visible_renderer_cannot_accept_sign_or_failure_pole():
    parameters = inspect.signature(observable_effect).parameters
    assert "sign" not in parameters
    assert "pole" not in parameters
    assert "action_state" in parameters


def test_candidate_and_future_surfaces_never_expose_authoring_scenario_ids():
    bank = build_bank()
    for episode in bank.private + bank.public:
        rendered = json.dumps(
            future_visible_surface(episode, bank.sidecar[episode["id"]]),
            sort_keys=True, ensure_ascii=False,
        )
        assert "XR-SCN-" not in rendered
        assert "At the the " not in rendered
        assert re.search(r"Available traces show[^.]*\bshows\b", rendered) is None
        assert "This route applies route " not in rendered


def test_future_surfaces_never_expose_path_plan_or_route_ordinals():
    bank = build_bank()
    forbidden = re.compile(
        r"\b(?:path|plan|route|option)\s*[- ]?\d+\b", re.IGNORECASE
    )
    for episode in bank.private + bank.public:
        rendered = json.dumps(
            future_visible_surface(episode, bank.sidecar[episode["id"]]),
            sort_keys=True, ensure_ascii=False,
        )
        assert forbidden.search(rendered) is None


def test_affordance_prose_has_no_mechanical_token_or_whitespace_padding():
    bank = build_bank()
    argument_key = {
        "notice": "message",
        "record": "change",
        "capacity": "purpose",
        "checkpoint": "agenda",
    }
    repeated_token_run = re.compile(r"\b([a-z]+)(?:\s+\1){2,}\b", re.IGNORECASE)
    for episode in bank.private + bank.public:
        hidden = bank.sidecar[episode["id"]]
        role_by_tool = {
            row["tool"]: hidden["path_tool_cues"][row["path_id"]]["action_role"]
            for row in hidden["path_specs"]
        }
        for affordance in episode["affordances"]:
            description = affordance["description"]
            action_text = affordance["arguments"][
                argument_key[role_by_tool[affordance["tool"]]]
            ]
            for text in (description, action_text):
                assert text == text.strip()
                assert text.endswith((".", "!", "?"))
                assert repeated_token_run.search(text) is None


def test_every_executable_role_agrees_with_its_stable_plan_and_argument_schema():
    bank = build_bank()
    argument_key = {
        "notice": "message",
        "record": "change",
        "capacity": "purpose",
        "checkpoint": "agenda",
    }
    for episode in bank.private + bank.public:
        hidden = bank.sidecar[episode["id"]]
        specs = {row["path_id"]: row for row in hidden["path_specs"]}
        assert set(hidden["path_tool_roles"]) == set(hidden["stable_action_plans"])
        for path_id, plan in hidden["stable_action_plans"].items():
            role = plan["action_role"]
            assert hidden["path_tool_roles"][path_id] == role
            assert argument_key[role] in specs[path_id]["arguments"]
            assert plan["plan_kind"].replace("_", " ") in next(
                row["description"] for row in episode["affordances"]
                if row["tool"] == specs[path_id]["tool"]
                and row["target"] == specs[path_id]["target"]
                and row["operation"] == specs[path_id]["operation"]
                and row["arguments"] == specs[path_id]["arguments"]
            )


def test_same_stable_action_phrase_flips_sign_only_when_required_state_changes():
    bank = build_bank()
    rows = defaultdict(list)
    for episode in bank.private:
        hidden = bank.sidecar[episode["id"]]
        for path_id, by_clause in hidden["semantic_bindings"].items():
            for clause, binding in by_clause.items():
                rows[(hidden["structure_id"], hidden["skin_id"], path_id, clause,
                      binding["evidence_text"])].append(binding["sign"])
    assert rows
    assert all(set(signs) == {-1, 1} for signs in rows.values())


def test_phrase_and_leave_one_family_decoders_stay_at_preregistered_floor():
    bank = build_bank()
    report = bank.sign_leak_audit
    assert report["gate_pass"] is True
    assert report["candidate_surface_violations"] == []
    assert report["observations"] == 600 * 4 * 4
    assert report["families"] == 40
    assert report["exact_phrase"]["pure_phrase_count"] == 0
    assert report["exact_phrase"]["majority_accuracy"] <= 0.60
    assert report["supported_token_purity"]["pure_token_count"] == 0
    assert report["leave_one_family_out"][
        "inversion_robust_predictability"
    ] <= 0.55


def test_neutrality_probe_fails_when_a_candidate_surface_gains_a_construct_label():
    bank = build_bank()
    episodes = bank.private
    episodes[0] = deepcopy(episodes[0])
    episodes[0]["multiturn_script"]["stage_1"][0]["content"] += (
        " This is the morally positive love choice."
    )
    report = audit(episodes, bank.sidecar, decoder_episodes=episodes)
    assert report["gate_pass"] is False
    assert any(row["kind"] == "valence_label"
               for row in report["candidate_surface_violations"])


def test_sign_leak_probe_rejects_authoring_scenario_identity():
    bank = build_bank()
    episodes = bank.private
    episodes[0] = deepcopy(episodes[0])
    episodes[0]["visible_consequences"].append(
        "Resolve XR-SCN-003-EVIDENCE-revision before close."
    )
    report = audit(episodes, bank.sidecar, decoder_episodes=episodes)
    assert report["gate_pass"] is False
    assert any(row["kind"] == "authoring_identifier"
               for row in report["candidate_surface_violations"])


def test_branch_effect_ordinals_and_causal_poles_are_exactly_balanced():
    bank = build_bank()
    ordinal = defaultdict(Counter)
    occurrences = defaultdict(set)
    for episode in bank.private:
        hidden = bank.sidecar[episode["id"]]
        for path_id, order in hidden["semantic_effect_order"].items():
            for position, clause in enumerate(order):
                ordinal[(clause, position)][hidden["path_keys"][path_id][clause]] += 1
            assert hidden["reaction_table"][path_id]["branch_effect_order"] == order
        assert hidden["reaction_table"]["evasion"]["branch_effect_order"] == []
        for path_id, by_clause in hidden["path_failure_poles"].items():
            for clause, pole in by_clause.items():
                occurrences[(hidden["consistency_group"], path_id, clause)].add(pole)
    assert len(ordinal) == 16 * 4
    assert all(counts[1] == counts[-1] for counts in ordinal.values())
    pole_counts = Counter(
        (clause, next(iter(poles)))
        for (_, _, clause), poles in occurrences.items()
    )
    assert all(pole_counts[(f"C{index}", pole)] == 50
               for index in range(1, 17)
               for pole in ("sentimental", "harsh"))
