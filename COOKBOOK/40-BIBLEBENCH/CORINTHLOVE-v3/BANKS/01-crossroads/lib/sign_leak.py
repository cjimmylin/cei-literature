"""Static semantic-neutrality and relational sign-decoder probes."""
from __future__ import annotations

from collections import Counter, defaultdict
from collections.abc import Mapping
import math
import re

from .registry import CLAUSE_ACTIONS, CLAUSE_REGISTRY
from .split_hygiene import future_visible_surface, normalized_core


EXACT_PHRASE_ACCURACY_CEILING = 0.60
HELDOUT_LEXICAL_ACCURACY_CEILING = 0.55
FORBIDDEN_VALENCE_RE = re.compile(
    r"\b(?:sentimental|harsh|positive|negative|benefits?|trade[- ]?offs?|"
    r"payback|gleeful|gullible|malice|overconfidence)\b|"
    r"\b(?:love|loving|charity|charitable|patience|patient|kindness|envy|"
    r"boast\w*|dignity|truth|hope\w*|endurance|humility|moral|virtue|vice)\b|"
    r"protects?\s+dignity|welcomes?\s+truth",
    re.IGNORECASE,
)
AUTHORING_ID_RE = re.compile(r"\bXR-SCN-[A-Z0-9-]+\b", re.IGNORECASE)
ANSWER_LABEL_RE = re.compile(
    r"\b(?:path|plan|route|option)\s*[- ]?\d+\b", re.IGNORECASE
)


def _strings(value):
    if isinstance(value, Mapping):
        for key, item in value.items():
            yield str(key)
            yield from _strings(item)
    elif isinstance(value, list):
        for item in value:
            yield from _strings(item)
    elif isinstance(value, str):
        yield value


def _tokens(text: str) -> set[str]:
    return {
        token for token in normalized_core(text).split()
        if len(token) >= 3 and token not in {
            "the", "and", "for", "this", "that", "with", "into", "from",
            "one", "two", "its", "also", "state", "plan", "route", "field",
        }
    }


def _observations(episodes: list, sidecar: Mapping) -> list[dict]:
    rows = []
    for episode in episodes:
        hidden = sidecar[episode["id"]]
        claims = {
            row["clause"]: row["visible_claim"]
            for row in hidden["competing_claims"]
        }
        for path_id, by_clause in hidden["semantic_bindings"].items():
            for clause, binding in by_clause.items():
                rows.append({
                    "family": hidden["template_family"],
                    "scenario_id": hidden["scenario_id"],
                    "path_id": path_id,
                    "clause": clause,
                    "text": normalized_core(binding["evidence_text"]),
                    "lexical_context": normalized_core(
                        f"{binding['evidence_text']} {claims[clause]}"
                    ),
                    "sign": binding["sign"],
                })
    return rows


def _registry_phrases() -> list[str]:
    phrases = []
    for row in CLAUSE_REGISTRY.values():
        phrases.extend((
            row["construct"], row["sentimental_pole"], row["harsh_pole"],
        ))
    for row in CLAUSE_ACTIONS.values():
        phrases.extend(row.values())
    return [normalized_core(row) for row in phrases]


def audit(episodes: list, sidecar: Mapping, decoder_episodes=None) -> dict:
    """Run preregistered exact-phrase and held-out-family lexical probes."""
    if not isinstance(episodes, list) or not isinstance(sidecar, Mapping):
        raise TypeError("sign leak audit requires episodes and sidecar")
    candidate_violations = []
    frozen_phrases = _registry_phrases()
    for episode in episodes:
        hidden = sidecar[episode["id"]]
        surface = future_visible_surface(episode, hidden)
        values = list(_strings(surface))
        rendered = normalized_core("\n".join(values))
        if FORBIDDEN_VALENCE_RE.search("\n".join(values)):
            candidate_violations.append({
                "item_id": episode["id"], "kind": "valence_label",
            })
        if AUTHORING_ID_RE.search("\n".join(values)):
            candidate_violations.append({
                "item_id": episode["id"], "kind": "authoring_identifier",
            })
        if ANSWER_LABEL_RE.search("\n".join(values)):
            candidate_violations.append({
                "item_id": episode["id"], "kind": "answer_label",
            })
        for phrase in frozen_phrases:
            if phrase and phrase in rendered:
                candidate_violations.append({
                    "item_id": episode["id"], "kind": "frozen_registry_phrase",
                    "phrase": phrase,
                })
                break
        field_labels = [
            key for key in _strings(surface)
            if FORBIDDEN_VALENCE_RE.fullmatch(key.strip())
        ]
        if field_labels:
            candidate_violations.append({
                "item_id": episode["id"], "kind": "valenced_field_label",
                "labels": field_labels,
            })

    observations = _observations(
        episodes if decoder_episodes is None else decoder_episodes, sidecar
    )
    for row in observations:
        row["lexical_tokens"] = _tokens(row["lexical_context"])
    phrase_counts = defaultdict(Counter)
    token_counts = defaultdict(Counter)
    for row in observations:
        phrase_counts[row["text"]][row["sign"]] += 1
        for token in _tokens(row["text"]):
            token_counts[token][row["sign"]] += 1
    pure_phrases = [
        phrase for phrase, counts in phrase_counts.items()
        if not counts[1] or not counts[-1]
    ]
    exact_accuracy = (
        sum(max(counts[1], counts[-1]) for counts in phrase_counts.values())
        / len(observations)
    )
    pure_supported_tokens = [
        {"token": token, "plus": counts[1], "minus": counts[-1]}
        for token, counts in token_counts.items()
        if counts[1] + counts[-1] >= 20 and (not counts[1] or not counts[-1])
    ]

    # Leave one scenario/template family out.  The fractional .5 credit for a
    # zero log-odds score is the preregistered chance treatment, not a random
    # tie-breaker.
    families = sorted({row["family"] for row in observations})
    global_lexical_counts = defaultdict(Counter)
    by_family = defaultdict(list)
    for row in observations:
        by_family[row["family"]].append(row)
        for token in row["lexical_tokens"]:
            global_lexical_counts[token][row["sign"]] += 1
    fractional_correct = 0.0
    evaluated = 0
    fold_rows = []
    for heldout in families:
        test = by_family[heldout]
        heldout_counts = defaultdict(Counter)
        for row in test:
            for token in row["lexical_tokens"]:
                heldout_counts[token][row["sign"]] += 1
        fold_correct = 0.0
        for row in test:
            score = sum(
                math.log(
                    (global_lexical_counts[token][1] - heldout_counts[token][1] + 1)
                    / (global_lexical_counts[token][-1] - heldout_counts[token][-1] + 1)
                )
                for token in row["lexical_tokens"]
            )
            if score == 0:
                credit = 0.5
            else:
                credit = float((1 if score > 0 else -1) == row["sign"])
            fold_correct += credit
        evaluated += len(test)
        fractional_correct += fold_correct
        fold_rows.append({
            "heldout_family": heldout,
            "observations": len(test),
            "fractional_accuracy": fold_correct / len(test),
        })
    heldout_accuracy = fractional_correct / evaluated
    heldout_predictability = max(heldout_accuracy, 1.0 - heldout_accuracy)
    gate_pass = (
        not candidate_violations
        and not pure_phrases
        and not pure_supported_tokens
        and exact_accuracy <= EXACT_PHRASE_ACCURACY_CEILING
        and heldout_predictability <= HELDOUT_LEXICAL_ACCURACY_CEILING
    )
    return {
        "gate_pass": gate_pass,
        "candidate_surface_violations": candidate_violations,
        "observations": len(observations),
        "families": len(families),
        "exact_phrase": {
            "unique_phrases": len(phrase_counts),
            "pure_phrase_count": len(pure_phrases),
            "majority_accuracy": exact_accuracy,
            "ceiling": EXACT_PHRASE_ACCURACY_CEILING,
        },
        "supported_token_purity": {
            "minimum_support": 20,
            "pure_token_count": len(pure_supported_tokens),
            "violations": pure_supported_tokens,
        },
        "leave_one_family_out": {
            "fractional_accuracy": heldout_accuracy,
            "inversion_robust_predictability": heldout_predictability,
            "ceiling": HELDOUT_LEXICAL_ACCURACY_CEILING,
            "folds": fold_rows,
        },
    }


def assert_clean(report: Mapping) -> None:
    assert isinstance(report, Mapping) and report.get("gate_pass") is True, (
        f"relational sign-leak audit failed: {report}"
    )
