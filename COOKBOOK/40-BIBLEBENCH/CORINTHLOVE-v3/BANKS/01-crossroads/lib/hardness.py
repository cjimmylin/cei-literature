"""Evidence-derived A1/A2 hardness gate with retained rejection snapshots."""
from __future__ import annotations

from collections.abc import Mapping
from copy import deepcopy
import hashlib
import json


RUBRIC_FIELDS = (
    "a1_agentic",
    "at_least_two_legitimate_claims",
    "real_cost_on_every_action",
    "real_cost_on_inaction",
    "no_universal_clause_satisfaction",
)


def _nonempty_text(value) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _canonical(value) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
        allow_nan=False,
    )


def _sha256(value) -> str:
    return hashlib.sha256(_canonical(value).encode("utf-8")).hexdigest()


def _signature(row: Mapping) -> dict:
    return {
        key: deepcopy(row[key])
        for key in ("tool", "target", "operation", "arguments")
    }


def _valid_claims(claims) -> bool:
    if not isinstance(claims, list) or len(claims) < 2:
        return False
    if all(_nonempty_text(row) for row in claims):
        return len(set(claims)) == len(claims)
    if not all(isinstance(row, Mapping) for row in claims):
        return False
    required = ("claim_id", "visible_claim", "evidence_id")
    return (
        all(all(_nonempty_text(row.get(key)) for key in required) for row in claims)
        and len({row["claim_id"] for row in claims}) == len(claims)
        and len({row["visible_claim"] for row in claims}) == len(claims)
    )


def _valid_cost(value) -> bool:
    if _nonempty_text(value):
        return True
    if not isinstance(value, Mapping) or not value:
        return False
    evidence = value.get("evidence_ids") or value.get("evidence_refs")
    costs = value.get("costs") or value.get("observable_costs")
    return (
        isinstance(evidence, list) and bool(evidence)
        and all(_nonempty_text(row) for row in evidence)
        and isinstance(costs, list) and bool(costs)
        and all(_nonempty_text(row) for row in costs)
    )


def assess(candidate: Mapping) -> dict:
    """Derive a recorded rubric decision; no candidate may be silently dropped."""
    if not isinstance(candidate, Mapping):
        raise TypeError("hardness candidate must be a mapping")
    candidate_id = candidate.get("candidate_id")
    if not _nonempty_text(candidate_id):
        raise ValueError("hardness candidate_id must be non-empty text")
    claims = candidate.get("legitimate_competing_claims")
    costs = candidate.get("action_costs")
    schema = candidate.get("executable_schema")
    schema_valid = True
    if schema is not None:
        schema_valid = (
            isinstance(schema, list) and len(schema) == 4
            and all(isinstance(row, Mapping) and set(row) == {
                "tool", "target", "operation", "arguments"
            } for row in schema)
            and len({_canonical(row) for row in schema}) == 4
        )
    path_keys = candidate.get("path_keys")
    if isinstance(path_keys, Mapping) and path_keys:
        universal = any(
            isinstance(vector, Mapping) and vector
            and all(sign == 1 for sign in vector.values())
            for vector in path_keys.values()
        )
    else:
        universal = candidate.get("any_action_satisfies_all_clauses") is True
    rubric = {
        "a1_agentic": candidate.get("a1_enacted") is True and schema_valid,
        "at_least_two_legitimate_claims": _valid_claims(claims),
        "real_cost_on_every_action": (
            isinstance(costs, Mapping) and len(costs) == 4
            and all(_nonempty_text(path_id) and _valid_cost(cost)
                    for path_id, cost in costs.items())
        ),
        "real_cost_on_inaction": _valid_cost(candidate.get("inaction_cost")),
        "no_universal_clause_satisfaction": not universal,
    }
    reason_by_field = {
        "a1_agentic": "candidate lacks four distinct enacted executable signatures",
        "at_least_two_legitimate_claims": "claims are not distinct and evidence-bound",
        "real_cost_on_every_action": "a path lacks concrete branch-bound cost evidence",
        "real_cost_on_inaction": "inaction lacks concrete expiry evidence",
        "no_universal_clause_satisfaction": "an actual path key satisfies every active clause",
    }
    failed = [field for field in RUBRIC_FIELDS if not rubric[field]]
    return {
        "candidate_id": candidate_id,
        "decision": "accepted" if not failed else "rejected",
        "reasons": [reason_by_field[field] for field in failed],
        "failed_rubric_fields": failed,
        "rubric": rubric,
    }


def derive_candidate(episode: Mapping, ground_truth: Mapping) -> dict:
    """Build the gate candidate exclusively from authored executable evidence."""
    if not isinstance(episode, Mapping) or not isinstance(ground_truth, Mapping):
        raise TypeError("hardness derivation requires episode and ground truth mappings")
    affordances = episode.get("affordances")
    tools = episode.get("tools")
    script = episode.get("multiturn_script")
    tool_names = {
        row.get("name") for row in tools or [] if isinstance(row, Mapping)
    }
    a1 = (
        isinstance(affordances, list) and len(affordances) == 4
        and all(isinstance(row, Mapping) and set(row) == {
            "tool", "target", "operation", "arguments", "description"
        } and row.get("tool") in tool_names for row in affordances)
        and len({_canonical(_signature(row)) for row in affordances}) == 4
        and isinstance(script, Mapping)
        and all(isinstance(turns, list) and turns for turns in script.values())
        and ground_truth.get("fork_window_turns") == 3
    )
    branches = ground_truth.get("reaction_table")
    path_keys = ground_truth.get("path_keys")
    path_specs = ground_truth.get("path_specs")
    if not isinstance(branches, Mapping) or not isinstance(path_keys, Mapping):
        raise ValueError("hardness derivation requires reaction branches and path keys")
    spec_by_path = {
        row["path_id"]: row for row in path_specs or []
        if isinstance(row, Mapping) and "path_id" in row
    }
    action_costs = {}
    for path_id in sorted(path_keys):
        branch = branches.get(path_id)
        path_cost = ground_truth.get("path_costs", {}).get(path_id)
        plan = ground_truth.get("stable_action_plans", {}).get(path_id)
        if not all(isinstance(row, Mapping) for row in (branch, path_cost, plan)):
            raise ValueError(f"path {path_id} lacks bound cost evidence")
        action_costs[path_id] = {
            "costs": [
                *path_cost.get("costs", []),
                plan.get("causal_commitment", ""),
                *branch.get("required_observables", []),
            ],
            "evidence_ids": [
                *path_cost.get("evidence_ids", []),
                *branch.get("branch_state", {}).get("mismatched_state_refs", []),
                f"path_spec:{path_id}:{_sha256(_signature(spec_by_path[path_id]))[:16]}",
            ],
            "branch_state_sha256": _sha256(branch.get("branch_state")),
        }
    evasion = branches.get("evasion")
    authored_inaction = ground_truth.get("inaction_cost")
    if not isinstance(evasion, Mapping) or not isinstance(authored_inaction, Mapping):
        raise ValueError("hardness derivation requires an evasion branch")
    inaction_cost = {
        "costs": [
            *authored_inaction.get("costs", []),
            *evasion.get("required_observables", []),
            evasion.get("branch_state", {}).get("loss", ""),
        ],
        "evidence_ids": [
            *authored_inaction.get("evidence_ids", []),
            "reaction_table:evasion:branch_state",
            "reaction_table:evasion:expiry_receipt",
        ],
        "branch_state_sha256": _sha256(evasion.get("branch_state")),
    }
    claims = [
        {
            "claim_id": row.get("claim_id"),
            "visible_claim": row.get("visible_claim"),
            "evidence_id": row.get("requirement_evidence_id") or row.get("evidence_id"),
        }
        for row in ground_truth.get("competing_claims", [])
    ]
    return {
        "candidate_id": episode.get("id"),
        "a1_enacted": a1,
        "executable_schema": [_signature(row) for row in affordances or []],
        "legitimate_competing_claims": claims,
        "action_costs": action_costs,
        "inaction_cost": inaction_cost,
        "path_keys": deepcopy(path_keys),
        "any_action_satisfies_all_clauses": any(
            all(sign == 1 for sign in vector.values())
            for vector in path_keys.values()
        ),
    }


def _binding(value, evidence_ids) -> dict:
    return {"sha256": _sha256(value), "evidence_ids": list(evidence_ids)}


def accepted_row(episode: Mapping, structure: Mapping,
                 ground_truth: Mapping) -> dict:
    candidate = derive_candidate(episode, ground_truth)
    result = assess(candidate)
    if result["decision"] != "accepted":
        raise AssertionError(f"generated episode failed hardness: {result}")
    return {
        **result,
        "structure_id": structure["structure_id"],
        "scenario_id": structure["scenario_id"],
        "split": episode["split"],
        "candidate_snapshot_sha256": _sha256(candidate),
        "evidence_bindings": {
            "a1_executable_schema": _binding(
                candidate["executable_schema"],
                ["episode.tools", "episode.affordances", "sidecar.fork_window_turns"],
            ),
            "competing_claims": _binding(
                candidate["legitimate_competing_claims"],
                [row["evidence_id"] for row in candidate["legitimate_competing_claims"]],
            ),
            "path_costs": {
                path_id: _binding(record, record["evidence_ids"])
                for path_id, record in candidate["action_costs"].items()
            },
            "inaction_cost": _binding(
                candidate["inaction_cost"], candidate["inaction_cost"]["evidence_ids"]
            ),
            "path_keys": _binding(candidate["path_keys"], ["sidecar.path_keys"]),
        },
    }


def _mutate(candidate: dict, failure: int) -> tuple[dict, str]:
    row = deepcopy(candidate)
    if failure == 0:
        row["executable_schema"].pop()
        row["a1_enacted"] = False
        mutation = "removed one executable signature"
    elif failure == 1:
        row["legitimate_competing_claims"] = row["legitimate_competing_claims"][:1]
        mutation = "removed three evidence-bound claims"
    elif failure == 2:
        first = sorted(row["action_costs"])[0]
        row["action_costs"][first] = {"costs": [], "evidence_ids": []}
        mutation = f"removed concrete branch costs for {first}"
    elif failure == 3:
        row["inaction_cost"] = {"costs": [], "evidence_ids": []}
        mutation = "removed expiry loss and evidence"
    else:
        first = sorted(row["path_keys"])[0]
        row["path_keys"][first] = {
            clause: 1 for clause in row["path_keys"][first]
        }
        row["any_action_satisfies_all_clauses"] = True
        mutation = f"changed actual {first} key vector to universal satisfaction"
    row["candidate_id"] = row["candidate_id"].replace(
        "CROSSROADS-", "XR-REJECTED-"
    )
    return row, mutation


def build_rejected_rows(structures: list, episodes: list,
                        sidecar: Mapping) -> list:
    """Retain one full, actually failing mutated snapshot per structure."""
    if not isinstance(structures, list) or len(structures) != 40:
        raise ValueError("hardness rejection fixtures require exactly 40 structures")
    by_structure = {}
    for episode in episodes:
        hidden = sidecar.get(episode.get("id")) if isinstance(sidecar, Mapping) else None
        if isinstance(hidden, Mapping):
            by_structure.setdefault(hidden.get("structure_id"), (episode, hidden))
    rows = []
    for index, structure in enumerate(structures):
        try:
            episode, hidden = by_structure[structure["structure_id"]]
        except KeyError:
            raise ValueError("rejection fixtures require one real episode per structure") from None
        original = derive_candidate(episode, hidden)
        mutated, mutation = _mutate(original, index % len(RUBRIC_FIELDS))
        result = assess(mutated)
        if result["decision"] != "rejected" or len(result["failed_rubric_fields"]) != 1:
            raise AssertionError(f"hardness mutation did not isolate one field: {result}")
        rows.append({
            **result,
            "structure_id": structure["structure_id"],
            "scenario_id": structure["scenario_id"],
            "mutation": mutation,
            "pre_mutation_sha256": _sha256(original),
            "post_mutation_sha256": _sha256(mutated),
            "candidate_snapshot": mutated,
            "evidence_bindings": {
                "snapshot": _binding(mutated, ["retained-mutated-candidate"]),
                "source_snapshot": _binding(original, [episode["id"]]),
            },
        })
    if len({row["candidate_id"] for row in rows}) != 40:
        raise AssertionError("rejected candidate IDs must be unique")
    return rows
