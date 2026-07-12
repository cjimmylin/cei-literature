"""Full-future-surface public/private split-hygiene audit."""
from __future__ import annotations

from collections.abc import Mapping
import hashlib
import json
import re


STAGES = ("stage_1", "stage_2", "stage_3", "stage_4")
FUTURE_VISIBLE_FIELDS = (
    "stages", "tools", "fork_affordances", "visible_consequences",
    "public_branch_states", "reaction_turns", "repair_affordances",
    "closeout_affordances",
)


def normalized_core(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("surface text must be a string")
    value = text.lower()
    value = re.sub(r"[0-9a-f]{8}-[0-9a-f-]{27,}", " <uuid> ", value)
    value = re.sub(r"\b(?:xr-scn|crossroads)-?\d+[a-z0-9-]*\b", " <case> ", value)
    value = re.sub(r"\d+", " <n> ", value)
    value = re.sub(r"[^a-z<>]+", " ", value)
    return " ".join(value.split())


def four_token_shingles(text: str) -> set[tuple[str, ...]]:
    shingles = set()
    # Scalar fields are separate candidate-visible utterances/identifiers;
    # never invent a lexical shingle by concatenating the end of one JSON field
    # with the beginning of another.
    for line in text.splitlines() or [text]:
        tokens = normalized_core(line).split()
        shingles.update(
            tuple(tokens[i:i + 4])
            for i in range(max(0, len(tokens) - 3))
        )
    return shingles


def containment(left: str, right: str) -> float:
    a, b = four_token_shingles(left), four_token_shingles(right)
    return 0.0 if not a or not b else len(a & b) / min(len(a), len(b))


def _script(row: Mapping) -> Mapping:
    script = row.get("multiturn_script")
    if not isinstance(script, Mapping) or set(script) != set(STAGES):
        raise ValueError("every episode needs exact stage_1..stage_4 turns")
    if any(not isinstance(script[stage], list) or not script[stage]
           for stage in STAGES):
        raise ValueError("every stage must be a non-empty turn list")
    return script


def future_visible_surface(episode: Mapping, hidden: Mapping) -> dict:
    """Project every surface that can become visible during an enacted run."""
    script = _script(episode)
    branches = hidden.get("reaction_table")
    if not isinstance(branches, Mapping) or set(branches) != (
            set(hidden.get("path_keys", {})) | {"evasion"}):
        raise ValueError("split audit requires every reaction branch")
    public_branch_states, reaction_turns, repair, closeout = [], [], [], []
    for branch_id in sorted(branches):
        branch = branches[branch_id]
        if not isinstance(branch, Mapping):
            raise ValueError("reaction branch must be a mapping")
        turns = branch.get("turns")
        repair_rows = branch.get("repair_affordances")
        close_rows = branch.get("closeout_affordances")
        if not isinstance(turns, list) or not turns:
            raise ValueError("reaction branch turns are missing")
        if not isinstance(repair_rows, list) or len(repair_rows) != 2:
            raise ValueError("reaction branch must expose two repair affordances")
        if not isinstance(close_rows, list) or len(close_rows) != 1:
            raise ValueError("reaction branch must expose one closeout affordance")
        reaction_turns.append(turns)
        public_state = branch.get("public_branch_state")
        if not isinstance(public_state, Mapping) or not public_state:
            raise ValueError("reaction branch public state is missing")
        public_branch_states.append(public_state)
        repair.append(repair_rows)
        closeout.append(close_rows)
    projected = {
        "stages": {stage: script[stage] for stage in STAGES},
        "tools": episode.get("tools"),
        "fork_affordances": episode.get("affordances"),
        "visible_consequences": episode.get("visible_consequences"),
        "public_branch_states": public_branch_states,
        "reaction_turns": reaction_turns,
        "repair_affordances": repair,
        "closeout_affordances": closeout,
    }
    if tuple(projected) != FUTURE_VISIBLE_FIELDS:
        raise AssertionError("future-visible split projection changed")
    if not all(isinstance(projected[field], (list, dict))
               for field in FUTURE_VISIBLE_FIELDS):
        raise ValueError("future-visible surface is incomplete")
    return projected


def _surface_text(episode: Mapping, hidden: Mapping) -> str:
    # Four-shingle leakage is a lexical audit over future-visible values, not
    # an audit of unavoidable JSON punctuation and shared envelope key names.
    # Tool names, operations, targets, descriptions, and every argument value
    # remain included because they are scalar values in this projection.
    values = []

    def walk(value):
        if isinstance(value, Mapping):
            for key in sorted(value):
                walk(value[key])
        elif isinstance(value, list):
            for row in value:
                walk(row)
        elif isinstance(value, str):
            values.append(value)
        elif value is not None:
            values.append(str(value))

    walk(future_visible_surface(episode, hidden))
    return "\n".join(values)


def audit(public: list, private: list, sidecar: Mapping,
          threshold: float = 0.25) -> dict:
    if not 0 < threshold <= 1:
        raise ValueError("threshold must lie in (0, 1]")
    if not isinstance(public, list) or not isinstance(private, list):
        raise TypeError("splits must be lists")
    all_rows = public + private
    ids = [row.get("id") for row in all_rows]
    if any(not isinstance(item_id, str) or not item_id for item_id in ids):
        raise ValueError("episode IDs must be non-empty strings")
    violations = []
    if len(ids) != len(set(ids)):
        violations.append({"kind": "id_overlap"})
    if any(row.get("split") != "public" for row in public):
        violations.append({"kind": "public_split_label"})
    if any(row.get("split") != "private" for row in private):
        violations.append({"kind": "private_split_label"})
    if not isinstance(sidecar, Mapping) or not set(ids).issubset(sidecar):
        raise ValueError("sidecar must cover both splits")

    for field, kind in (
            ("skin_id", "skin_overlap"),
            ("parameter_region_id", "parameter_region_overlap")):
        left = {sidecar[row["id"]].get(field) for row in public}
        right = {sidecar[row["id"]].get(field) for row in private}
        if None in left or None in right:
            raise ValueError(f"sidecar is missing {field}")
        overlap = left & right
        if overlap:
            violations.append({"kind": kind, "values": sorted(overlap)})

    public_text = {
        row["id"]: _surface_text(row, sidecar[row["id"]]) for row in public
    }
    private_text = {
        row["id"]: _surface_text(row, sidecar[row["id"]]) for row in private
    }
    public_hashes = {
        item_id: hashlib.sha256(normalized_core(text).encode()).hexdigest()
        for item_id, text in public_text.items()
    }
    private_hashes = {
        item_id: hashlib.sha256(normalized_core(text).encode()).hexdigest()
        for item_id, text in private_text.items()
    }
    public_shingles = {
        item_id: four_token_shingles(text) for item_id, text in public_text.items()
    }
    private_shingles = {
        item_id: four_token_shingles(text) for item_id, text in private_text.items()
    }
    comparisons = 0
    maximum = 0.0
    maximum_pair = None
    for public_id, left in public_text.items():
        for private_id, right in private_text.items():
            comparisons += 1
            left_shingles = public_shingles[public_id]
            right_shingles = private_shingles[private_id]
            score = (
                0.0 if not left_shingles or not right_shingles else
                len(left_shingles & right_shingles)
                / min(len(left_shingles), len(right_shingles))
            )
            if score > maximum:
                maximum = score
                maximum_pair = {"public_id": public_id, "private_id": private_id}
            if public_hashes[public_id] == private_hashes[private_id] or score >= threshold:
                violations.append({
                    "kind": "full_surface_overlap",
                    "public_id": public_id,
                    "private_id": private_id,
                    "containment": score,
                    "exact_hash_match": public_hashes[public_id] == private_hashes[private_id],
                })
    return {
        "counts": {"public": len(public), "private": len(private)},
        "threshold": threshold,
        "comparison_scope": "all-public-x-all-private",
        "future_visible_fields": list(FUTURE_VISIBLE_FIELDS),
        "shingle_width": 4,
        "comparisons": comparisons,
        "max_containment": maximum,
        "max_pair": maximum_pair,
        "public_surface_hashes": public_hashes,
        "private_surface_hashes": private_hashes,
        "violations": violations,
    }


def assert_clean(report: Mapping) -> None:
    assert isinstance(report, Mapping), "split hygiene report is missing"
    assert not report.get("violations"), (
        f"split hygiene failed: {report.get('violations', [])[:5]}"
    )
