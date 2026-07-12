from __future__ import annotations

from collections import Counter, defaultdict
import json
import re

from generator import build_bank
from lib.registry import CLAUSES
from lib.scenarios import mismatch_pole


SIGN_ROLE_LABEL_RE = re.compile(
    r"\b(?:benefits?|trade-?offs?|positive|negative)\b", re.IGNORECASE
)


def _specs_by_path(hidden: dict) -> dict:
    return {row["path_id"]: row for row in hidden["path_specs"]}


def test_every_hidden_key_is_bound_to_exact_visible_clause_action_evidence():
    bank = build_bank()
    for episode in bank.private + bank.public:
        hidden = bank.sidecar[episode["id"]]
        specs = _specs_by_path(hidden)
        bindings = hidden.get("semantic_bindings")
        assert isinstance(bindings, dict)
        assert set(bindings) == set(hidden["path_keys"]) == set(specs)

        for path_id, vector in hidden["path_keys"].items():
            by_clause = bindings[path_id]
            assert set(by_clause) == set(hidden["clauses"]) == set(vector)
            rendered_action = json.dumps(
                specs[path_id], sort_keys=True, ensure_ascii=False
            )
            evidence_ids = []
            for clause, sign in vector.items():
                binding = by_clause[clause]
                assert set(binding) == {
                    "sign", "pole", "evidence_id", "evidence_text",
                }
                assert binding["sign"] == sign
                action_state = hidden["action_states"][path_id][clause]
                required_state = hidden["parameter_state"]["required_states"][clause]
                assert sign == (1 if action_state == required_state else -1)
                expected_poles = {"positive"} if sign == 1 else {
                    "sentimental", "harsh",
                }
                assert binding["pole"] in expected_poles
                if sign == -1:
                    expected, rationale = mismatch_pole(
                        clause=clause, required_state=required_state,
                        action_state=action_state,
                    )
                    assert binding["pole"] == expected
                    assert hidden["path_failure_rationales"][path_id][clause] == rationale
                assert binding["evidence_text"] in rendered_action
                assert binding["evidence_id"] in rendered_action
                evidence_ids.append(binding["evidence_id"])
            assert len(evidence_ids) == len(set(evidence_ids)) == 4


def test_negative_keys_counterbalance_both_frozen_failure_poles_per_clause():
    bank = build_bank()
    counts = Counter()
    for episode in bank.private:
        hidden = bank.sidecar[episode["id"]]
        for by_clause in hidden["semantic_bindings"].values():
            for clause, binding in by_clause.items():
                if binding["sign"] == -1:
                    counts[(clause, binding["pole"])] += 1

    assert {clause for clause, _ in counts} == set(CLAUSES)
    for clause in CLAUSES:
        assert counts[(clause, "sentimental")] > 0
        assert counts[(clause, "harsh")] > 0
        assert abs(
            counts[(clause, "sentimental")]
            - counts[(clause, "harsh")]
        ) <= 2


def test_matched_private_skins_preserve_keys_action_semantics_and_defeat_class():
    bank = build_bank()
    groups = defaultdict(list)
    for episode in bank.private:
        hidden = bank.sidecar[episode["id"]]
        groups[hidden["consistency_group"]].append((episode, hidden))

    assert len(groups) == 200
    assert {len(rows) for rows in groups.values()} == {3}
    for rows in groups.values():
        baseline = rows[0][1]
        for _, hidden in rows[1:]:
            assert hidden["path_keys"] == baseline["path_keys"]
            assert hidden["action_states"] == baseline["action_states"]
            assert hidden["stable_action_plans"] == baseline["stable_action_plans"]
            assert hidden["path_failure_poles"] == baseline[
                "path_failure_poles"
            ]
            assert hidden["path_failure_rationales"] == baseline[
                "path_failure_rationales"
            ]
            assert {
                branch: row["public_branch_state"]
                for branch, row in hidden["reaction_table"].items()
            } == {
                branch: row["public_branch_state"]
                for branch, row in baseline["reaction_table"].items()
            }

        # Skin arms remain genuine surface counterbalances, not duplicates.
        cue_schedules = {
            tuple(
                (path_id,) + tuple(
                    hidden["surface_cues"][path_id][axis]
                    for axis in ("warmth", "effort", "specificity", "length")
                )
                for path_id in sorted(hidden["surface_cues"])
            )
            for _, hidden in rows
        }
        tool_schedules = {
            tuple((row["path_id"], row["tool"])
                  for row in hidden["path_specs"])
            for _, hidden in rows
        }
        order_schedules = {
            tuple(hidden["path_order"])
            for _, hidden in rows
        }
        assert len(cue_schedules) == 3
        assert len(tool_schedules) == 3
        assert len(order_schedules) == 3


def test_private_unique_defeat_occurrences_are_skin_invariant_and_exactly_balanced():
    bank = build_bank()
    occurrences = defaultdict(set)
    for episode in bank.private:
        hidden = bank.sidecar[episode["id"]]
        for path_id, poles in hidden["path_failure_poles"].items():
            for clause, pole in poles.items():
                occurrence = (
                    hidden["consistency_group"], path_id, clause,
                )
                occurrences[occurrence].add(pole)

    # 200 structure/parameter cells x four paths x two negative clauses.
    assert len(occurrences) == 1600
    assert {len(poles) for poles in occurrences.values()} == {1}
    counts = Counter(
        (clause, next(iter(poles)))
        for (_, _, clause), poles in occurrences.items()
    )
    for clause in CLAUSES:
        assert counts[(clause, "sentimental")] == 50
        assert counts[(clause, "harsh")] == 50


def test_candidate_effect_statements_are_unlabeled_and_sign_balanced_by_ordinal():
    bank = build_bank()
    counts = defaultdict(Counter)
    for episode in bank.private + bank.public:
        rendered = json.dumps(episode, sort_keys=True, ensure_ascii=False)
        assert SIGN_ROLE_LABEL_RE.search(rendered) is None

    for episode in bank.private:
        hidden = bank.sidecar[episode["id"]]
        specs = _specs_by_path(hidden)
        for path_id, bindings in hidden["semantic_bindings"].items():
            evidence = specs[path_id]["arguments"]["effect_evidence"]
            assert len(evidence) == 4
            by_ref = {
                binding["evidence_id"]: (clause, binding)
                for clause, binding in bindings.items()
            }
            assert {row["ref"] for row in evidence} == set(by_ref)

            description = next(
                row["description"] for row in episode["affordances"]
                if row["tool"] == specs[path_id]["tool"]
                and row["target"] == specs[path_id]["target"]
                and row["operation"] == specs[path_id]["operation"]
                and row["arguments"] == specs[path_id]["arguments"]
            )
            positions = []
            for ordinal, row in enumerate(evidence):
                clause, binding = by_ref[row["ref"]]
                assert row["effect"] == binding["evidence_text"]
                positions.append(description.index(row["effect"]))
                counts[(clause, ordinal)][binding["sign"]] += 1
            assert positions == sorted(positions)

    assert set(clause for clause, _ in counts) == set(CLAUSES)
    assert {ordinal for _, ordinal in counts} == {0, 1, 2, 3}
    assert all(values[1] and values[-1] for values in counts.values())
    assert all(abs(values[1] - values[-1]) == 0
               for values in counts.values())


def test_visible_bank_never_serializes_hidden_semantic_map_or_clause_signs():
    bank = build_bank()
    for episode in bank.private + bank.public:
        rendered = json.dumps(episode, sort_keys=True, ensure_ascii=False)
        assert "semantic_bindings" not in rendered
        assert "path_failure_poles" not in rendered
        assert '"sign"' not in rendered
        assert all(f'"C{index}"' not in rendered for index in range(1, 17))
