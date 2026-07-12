from __future__ import annotations

from collections import Counter, defaultdict
import json
import re
import uuid

from generator import PUBLIC_DESIGN_SCHEDULE, build_bank, write_bank
from lib.canary import CANARY_RE, JSEED_RE
from lib.registry import CLAUSES


FORBIDDEN_PUBLIC_FIELDS = {
    "path_id", "path_keys", "clause_keys", "key_plus", "key_minus",
    "parameter_state", "parameter_region_id", "reaction_table",
    "hidden_state", "ground_truth", "judge_id", "judge_ids",
}
AFFORDANCE_FIELDS = {
    "tool", "target", "operation", "arguments", "description",
}


def walk_keys(value):
    if isinstance(value, dict):
        for key, item in value.items():
            yield key
            yield from walk_keys(item)
    elif isinstance(value, list):
        for item in value:
            yield from walk_keys(item)


def test_exact_scale_split_and_hardness_accounting_are_fail_loud():
    bank = build_bank()
    assert len(bank.private) == 600
    assert len(bank.public) == 30
    assert len(bank.sidecar) == 630
    assert len(bank.hardness_log) == 670
    assert Counter(row["decision"] for row in bank.hardness_log) == {
        "accepted": 630, "rejected": 40,
    }
    assert set(Counter(
        bank.sidecar[row["id"]]["structure_id"] for row in bank.private
    ).values()) == {15}
    assert len({row["id"] for row in bank.private + bank.public}) == 630


def test_public_design_varies_requirements_and_fails_loud_on_every_cue_cell():
    bank = build_bank()
    observed = [
        (
            next(i for i, structure in enumerate(bank.structures)
                 if structure["structure_id"] == bank.sidecar[row["id"]]["structure_id"]),
            bank.sidecar[row["id"]]["parameter_state"]["index"],
        )
        for row in bank.public
    ]
    assert observed == list(PUBLIC_DESIGN_SCHEDULE)
    assert len(set(observed)) == 30
    assert len({parameter for _, parameter in observed}) == 6
    assert bank.public_cue_audit["minimum_clause_episodes"] >= 6
    assert bank.public_cue_audit["max_cell_sign_association"] <= 0.15
    assert bank.public_cue_audit["max_standalone_adversarial_association"] <= 0.10
    assert bank.public_cue_audit["violations"] == []


def test_every_episode_is_enacted_multiturn_and_truth_stays_sidecar_only():
    bank = build_bank()
    turn_counts = set()
    tool_names = set()
    operations = set()
    substrate_schemas = set()
    for episode in bank.private + bank.public:
        stages = episode["multiturn_script"]
        assert set(stages) == {f"stage_{index}" for index in range(1, 5)}
        assert all(isinstance(stages[name], list) and stages[name]
                   for name in stages)
        total_turns = sum(len(turns) for turns in stages.values())
        assert 8 <= total_turns <= 20
        turn_counts.add(total_turns)
        assert 3 <= len(stages["stage_3"]) <= 8
        assert len(episode["affordances"]) == 4
        assert all(set(row) == AFFORDANCE_FIELDS for row in episode["affordances"])
        tool_names.update(row["name"] for row in episode["tools"])
        operations.update(row["operation"] for row in episode["affordances"])

        hidden = bank.sidecar[episode["id"]]
        substrate_schemas.add(hidden["substrate_schema_id"])
        assert set(hidden["path_keys"]) == {
            row["path_id"] for row in hidden["path_specs"]
        }
        assert len(hidden["path_specs"]) == 4
        assert hidden["evasion_key"] == {
            clause: -1 for clause in hidden["clauses"]
        }
        assert hidden["evasion_paths"] == []
        visible_signatures = {
            (row["tool"], row["target"], row["operation"],
             json.dumps(row["arguments"], sort_keys=True))
            for row in episode["affordances"]
        }
        hidden_signatures = {
            (row["tool"], row["target"], row["operation"],
             json.dumps(row["arguments"], sort_keys=True))
            for row in hidden["path_specs"]
        }
        assert visible_signatures == hidden_signatures
        for branch_id, branch in hidden["reaction_table"].items():
            assert len(branch["repair_affordances"]) == 2
            assert len(branch["closeout_affordances"]) == 1
            assert branch["public_branch_state"]
            assert branch["positive_duty_evidence"]["baseline_duty"]
            assert all(set(row) == AFFORDANCE_FIELDS for row in (
                branch["repair_affordances"] + branch["closeout_affordances"]
            ))
            if branch_id == "evasion":
                assert branch["branch_effect_order"] == []
            else:
                assert branch["branch_effect_order"] == hidden[
                    "semantic_effect_order"
                ][branch_id]

    assert turn_counts == {9, 10, 11, 12}
    assert 8 <= len(tool_names) <= 24
    assert len(operations) >= 16
    assert len(substrate_schemas) == 4

    for episode in bank.public:
        assert not (set(walk_keys(episode)) & FORBIDDEN_PUBLIC_FIELDS)
        rendered = json.dumps(episode, sort_keys=True)
        assert re.search(r"\bC(?:[1-9]|1[0-6])\s*[+-]", rendered) is None
        assert "10CB3-01-" in episode["canary"]
        assert "option A" not in rendered and '"A"' not in rendered


def test_key_balance_canaries_authoring_seeds_and_heldout_split_contracts():
    bank = build_bank()
    canaries = [row["canary"] for row in bank.private + bank.public]
    judge_tokens = list(bank.judge_seed_map)
    assert len(set(canaries)) == 630
    assert len(set(judge_tokens)) == 630
    assert all(CANARY_RE.fullmatch(value) for value in canaries)
    assert all(uuid.UUID(value.removeprefix("10CB3-01-")).version == 4
               for value in canaries)
    assert all(JSEED_RE.fullmatch(value) for value in judge_tokens)
    assert all(uuid.UUID(value.removeprefix("JSEED-")).version == 4
               for value in judge_tokens)
    assert set(bank.judge_seed_map.values()) == {
        row["id"] for row in bank.private + bank.public
    }

    public_skin_ids = {bank.sidecar[row["id"]]["skin_id"] for row in bank.public}
    private_skin_ids = {bank.sidecar[row["id"]]["skin_id"] for row in bank.private}
    public_regions = {
        bank.sidecar[row["id"]]["parameter_region_id"] for row in bank.public
    }
    private_regions = {
        bank.sidecar[row["id"]]["parameter_region_id"] for row in bank.private
    }
    assert public_skin_ids.isdisjoint(private_skin_ids)
    assert public_regions.isdisjoint(private_regions)

    cue_signs = defaultdict(Counter)
    for episode in bank.private:
        hidden = bank.sidecar[episode["id"]]
        for position, visible in enumerate(episode["affordances"]):
            signature = (
                visible["tool"], visible["target"], visible["operation"],
                json.dumps(visible["arguments"], sort_keys=True),
            )
            path_id = next(
                spec["path_id"] for spec in hidden["path_specs"]
                if (spec["tool"], spec["target"], spec["operation"],
                    json.dumps(spec["arguments"], sort_keys=True)) == signature
            )
            for clause, sign in hidden["path_keys"][path_id].items():
                cues = hidden["surface_cues"][path_id]
                for axis in ("warmth", "effort", "specificity", "length"):
                    cue_signs[(axis, clause, cues[axis])][sign] += 1
                cue_signs[("tool", clause, visible["tool"])][sign] += 1
                cue_signs[("ordinal", clause, position)][sign] += 1
    assert {axis for axis, _, _ in cue_signs} == {
        "warmth", "effort", "specificity", "length", "tool", "ordinal",
    }
    assert set(clause for _, clause, _ in cue_signs) == set(CLAUSES)
    assert all(abs(counts[1] - counts[-1]) <= 2
               for counts in cue_signs.values())
    assert bank.cue_audit["axes"] == {
        "warmth", "effort", "specificity", "length", "tool", "ordinal",
    }
    assert bank.cue_audit["max_absolute_sign_imbalance"] <= 2
    assert bank.cue_audit["coherent_action_axes"] == [
        "action_role", "tool", "operation", "target_kind",
    ]
    assert bank.cue_audit["max_coherent_action_sign_association"] <= 0.10


def test_sixty_stated_pairs_are_matched_counterbalanced_and_nonprimary():
    bank = build_bank()
    pairs = bank.stated_pairs
    assert len(pairs) == 60
    assert len({row["pair_id"] for row in pairs}) == 60
    assert len({row["enacted_item_id"] for row in pairs}) == 60
    assert Counter(row["order"] for row in pairs) == {
        "stated_first": 30, "enacted_first": 30,
    }
    episodes = {row["id"]: row for row in bank.private + bank.public}
    for row in pairs:
        assert row["primary_scoring_excluded"] is True
        stated = row["stated_item"]
        assert isinstance(stated, dict) and stated["vignette"].strip()
        enacted = episodes[row["enacted_item_id"]]
        assert Counter(
            json.dumps(value, sort_keys=True) for value in stated["affordances"]
        ) == Counter(
            json.dumps(value, sort_keys=True) for value in enacted["affordances"]
        )
        assert stated["path_keys"] == bank.sidecar[row["enacted_item_id"]]["path_keys"]


def test_write_bank_is_deterministic_and_registry_is_idempotent(tmp_path):
    bank = build_bank()
    root = tmp_path / "bank"
    registry = tmp_path / "canary_registry.txt"
    summary = write_bank(bank, bank_root=root, registry_path=registry)
    before = registry.read_bytes()
    assert summary == {
        "private": 600, "public": 30, "accepted": 630,
        "rejected": 40, "structures": 40,
    }
    assert len(registry.read_text().splitlines()) == 630
    write_bank(bank, bank_root=root, registry_path=registry)
    assert registry.read_bytes() == before
    assert len(json.loads((root / "deep_structures.yaml").read_text())) == 40
    assert len(json.loads((root / "episodes/private.yaml").read_text())) == 600
    assert len(json.loads((root / "seeds_public.yaml").read_text())) == 30
    assert len(json.loads((root / "sidecar/ground_truth.json").read_text())) == 630
    assert len(json.loads((root / "sidecar/judge_token_map.json").read_text())) == 630
    assert len(json.loads((root / "sidecar/stated_pairs.json").read_text())) == 60
    assert len((root / "sidecar/hardness_gate_log.jsonl").read_text().splitlines()) == 670
    split_report = json.loads((root / "reports/split_hygiene.json").read_text())
    sign_report = json.loads((root / "reports/sign_leak_probe.json").read_text())
    assert split_report["max_containment"] < 0.25
    assert split_report["violations"] == []
    assert sign_report["gate_pass"] is True
