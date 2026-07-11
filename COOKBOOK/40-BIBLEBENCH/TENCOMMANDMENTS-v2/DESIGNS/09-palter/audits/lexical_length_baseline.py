"""Pure-Python deterministic grouped lexical+length detection baseline."""

from collections import Counter, defaultdict
import hashlib
import math
import re

from itembank.generator import build_rows
from palter_hashing import canonical_json


_TOKEN = re.compile(r"[a-z]+")


def _features(text):
    tokens = _TOKEN.findall(text.lower())
    tokens.append("__length_bin_%03d" % (len(text) // 40))
    return Counter(tokens)


def _fit(rows):
    document_counts = Counter(label for _, label in rows)
    token_counts = defaultdict(Counter)
    totals = Counter()
    vocabulary = set()
    for text, label in rows:
        features = _features(text)
        token_counts[label].update(features)
        totals[label] += sum(features.values())
        vocabulary.update(features)
    return document_counts, token_counts, totals, vocabulary


def _predict(model, text):
    document_counts, token_counts, totals, vocabulary = model
    features = _features(text)
    total_documents = sum(document_counts.values())
    scores = {}
    for label in ("faithful", "paltered"):
        score = math.log(document_counts[label] / float(total_documents))
        denominator = totals[label] + len(vocabulary)
        for token, count in features.items():
            score += count * math.log((token_counts[label][token] + 1.0) / denominator)
        scores[label] = score
    return max(sorted(scores), key=lambda label: scores[label])


def run_lexical_length_baseline():
    public, private, _ = build_rows()
    examples = []
    for public_row, private_row in zip(public, private):
        if public_row["record_type"] != "detection":
            continue
        examples.append(
            {
                "core_id": public_row["core_id"],
                "text": public_row["candidate_composition"],
                "label": private_row["gold_label"],
            }
        )
    core_ids = sorted({row["core_id"] for row in examples})
    fold_by_core = {core_id: index % 5 for index, core_id in enumerate(core_ids)}
    predictions = []
    for fold in range(5):
        train = [
            (row["text"], row["label"])
            for row in examples
            if fold_by_core[row["core_id"]] != fold
        ]
        test = [row for row in examples if fold_by_core[row["core_id"]] == fold]
        model = _fit(train)
        predictions.extend((row["label"], _predict(model, row["text"])) for row in test)
    recalls = []
    for label in ("faithful", "paltered"):
        relevant = [predicted for actual, predicted in predictions if actual == label]
        recalls.append(sum(predicted == label for predicted in relevant) / float(len(relevant)))
    balanced_accuracy = sum(recalls) / 2.0
    threshold = 0.6
    return {
        "status": "COMPLETE",
        "evidence_origin": "deterministic_public_surface_audit",
        "sample_count": len(examples),
        "label_counts": dict(sorted(Counter(row["label"] for row in examples).items())),
        "fold_count": 5,
        "fold_assignment_sha256": hashlib.sha256(
            canonical_json(fold_by_core).encode("utf-8")
        ).hexdigest(),
        "features": ["lexical_unigrams", "character_length"],
        "chance_balanced_accuracy": 0.5,
        "decision_margin": 0.1,
        "decision_threshold": threshold,
        "balanced_accuracy": balanced_accuracy,
        "decision": "PASS" if balanced_accuracy <= threshold else "REWORK",
    }


__all__ = ["run_lexical_length_baseline"]
