"""Pre-registered family-stratified CHARITROC analysis pipeline."""
from __future__ import annotations

from collections import defaultdict

from analysis import roc


PROVENANCE = "harness validation, NOT a measurement"
REQUIRED_PRIMARY_FIELDS = {
    "item_family", "label", "stage4_score", "pair_id", "base_rate_benign",
}


def analyze_model(rows: list, bootstrap_draws: int = 2000,
                  seed: int = 20260709) -> dict:
    """Estimate family AUCs, random-effects pool, priors, and legacy tails.

    Only ``stage4_score`` is accepted as the primary score. Stage-3 update
    records use ``aggregate_stage3`` and cannot enter this function implicitly.
    """
    if not rows:
        raise ValueError("no scored rows")
    for index, row in enumerate(rows):
        missing = REQUIRED_PRIMARY_FIELDS - set(row)
        if missing:
            raise ValueError(f"row {index} missing stage4_score/primary fields: {sorted(missing)}")

    by_family = defaultdict(list)
    by_prior = defaultdict(list)
    for row in rows:
        by_family[row["item_family"]].append(row)
        by_prior[row["base_rate_benign"]].append(row)

    family_auc = {}
    for family, family_rows in sorted(by_family.items()):
        labels = [row["label"] for row in family_rows]
        if set(labels) != {0, 1}:
            raise ValueError(f"{family} requires both benign and malicious trials")
        estimate = roc.clustered_bootstrap_auc(
            labels,
            [row["stage4_score"] for row in family_rows],
            clusters=[row["pair_id"] for row in family_rows],
            draws=bootstrap_draws,
            seed=seed + len(family_auc),
        )
        family_auc[family] = {
            **estimate,
            "n_benign": labels.count(1),
            "n_malicious": labels.count(0),
        }

    hierarchical = roc.random_effects_pool({
        family: {
            "auc": estimate["auc"],
            "se": max(estimate["se"], roc.LOGIT_SE_FLOOR),
        }
        for family, estimate in family_auc.items()
    })

    operating = {}
    for prior, prior_rows in sorted(by_prior.items()):
        operating[str(prior)] = roc.evaluate_operating_points(
            [row["label"] for row in prior_rows],
            [row["stage4_score"] for row in prior_rows],
            base_rate_benign=float(prior),
        )

    labels = [row["label"] for row in rows]
    scores = [row["stage4_score"] for row in rows]
    return {
        "provenance": PROVENANCE,
        "family_auc": family_auc,
        "hierarchical_pool": hierarchical,
        "operating_points_by_prior": operating,
        "legacy_tails": roc.legacy_tail_rates(labels, scores),
        "primary_score_field": "stage4_score",
        "stage3_in_primary": False,
    }


def aggregate_stage3(records: list) -> dict:
    """Aggregate the D-07 update channel independently of discrimination."""
    if not records:
        raise ValueError("no stage-3 records")
    by_cue = defaultdict(list)
    all_values = []
    for index, record in enumerate(records):
        if "update_correct" not in record or "cue_variant" not in record:
            raise ValueError(f"stage-3 row {index} missing fields")
        value = record["update_correct"]
        if not isinstance(value, bool):
            raise ValueError(f"stage-3 row {index} is not mechanically resolved")
        all_values.append(value)
        by_cue[record["cue_variant"]].append(value)
    return {
        "provenance": PROVENANCE,
        "n": len(records),
        "accuracy": sum(all_values) / len(all_values),
        "by_cue": {
            cue: {"n": len(values), "accuracy": sum(values) / len(values)}
            for cue, values in sorted(by_cue.items())
        },
        "reported_separately_from_auc": True,
    }
