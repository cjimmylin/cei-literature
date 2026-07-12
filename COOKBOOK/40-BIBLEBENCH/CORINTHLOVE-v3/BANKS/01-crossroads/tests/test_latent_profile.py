from itertools import combinations
from pathlib import Path

import pytest

from analysis.latent_profile import (
    audit_block_information,
    fit_latent_profile,
    within_clause_irt_status,
)
from lib.blocks import build_deep_structures


def complete_pair_blocks():
    blocks = []
    for left, right in combinations(range(1, 17), 2):
        blocks.append({
            "structure_id": f"C{left}-C{right}",
            "path_keys": {
                "left": {f"C{left}": 1, f"C{right}": -1},
                "right": {f"C{left}": -1, f"C{right}": 1},
            },
        })
    return blocks


def actual_design_rows(model_id="model-a", repeats=5):
    rows = []
    for structure in build_deep_structures():
        path_keys = {
            path["path_id"]: dict(path["clause_keys"])
            for path in structure["base_paths"]
        }
        for repeat in range(repeats):
            rows.append({
                "model_id": model_id,
                "structure_id": structure["structure_id"],
                "outcome_type": "resolved",
                "path_keys": path_keys,
                "selected_path": f"path-{repeat % 4}",
            })
    return rows


def test_block_information_has_sum_zero_rank_and_complete_pair_coverage():
    audit = audit_block_information(
        complete_pair_blocks(), min_rank=15, min_pair_coverage=1,
        min_clause_blocks=15,
    )
    assert audit["rank"] == 15
    assert audit["identification_constraint"] == "sum(theta)=0"
    assert audit["minimum_pair_coverage"] == 1
    assert audit["minimum_clause_blocks"] == 15
    assert audit["gate_pass"] is True


def test_information_rank_is_computed_inside_the_sum_zero_subspace():
    blocks = [{
        "structure_id": f"axis-{index}",
        "path_keys": {
            "plus": {f"C{index}": 1},
            "minus": {f"C{index}": -1},
        },
    } for index in range(1, 17)]
    audit = audit_block_information(
        blocks, min_rank=15, min_pair_coverage=0, min_clause_blocks=1,
    )
    assert audit["rank"] == 15
    assert audit["maximum_identifiable_rank"] == 15


def test_small_public_panels_do_not_trigger_within_clause_irt():
    status = within_clause_irt_status(
        n_respondents=30, n_items=25, minimum_responses_per_item=30
    )
    assert status == {
        "status": "not_estimable",
        "reason": "requires at least 50 independent respondents",
        "exploratory_only": True,
    }


def test_within_clause_irt_requires_all_predeclared_floors():
    status = within_clause_irt_status(
        n_respondents=50, n_items=20, minimum_responses_per_item=30
    )
    assert status["status"] == "eligible_exploratory"
    assert status["exploratory_only"] is True


def test_latent_fit_requires_one_model_and_complete_actual_design():
    fitted = fit_latent_profile(actual_design_rows(), l2=1.0)
    assert fitted["model_id"] == "model-a"
    assert fitted["n_rows"] == 200
    assert fitted["n_structures"] == 40
    assert fitted["information_rank"] == 15
    assert fitted["status"] == "estimable_exploratory"


def test_latent_fit_rejects_cross_model_pooling_and_too_few_rows():
    rows = actual_design_rows()
    rows[-1]["model_id"] = "model-b"
    with pytest.raises(ValueError, match="exactly one model_id"):
        fit_latent_profile(rows)
    with pytest.raises(ValueError, match="at least 200 rows"):
        fit_latent_profile(actual_design_rows()[:-1])


@pytest.mark.parametrize("mutation,match", [
    ("missing_structure", "complete expected coverage"),
    ("fake_structure", "actual structure IDs"),
    ("evasion", "resolved outcomes only"),
    ("ambiguous", "resolved outcomes only"),
])
def test_latent_fit_rejects_incomplete_or_nonresolved_measurement(mutation, match):
    rows = actual_design_rows()
    if mutation == "missing_structure":
        missing = rows[0]["structure_id"]
        rows = [row for row in rows if row["structure_id"] != missing]
        rows.extend(dict(rows[0]) for _ in range(5))
    elif mutation == "fake_structure":
        rows[0]["structure_id"] = "XR-DS-999"
    else:
        rows[0]["outcome_type"] = mutation
        rows[0]["selected_path"] = None
    with pytest.raises(ValueError, match=match):
        fit_latent_profile(rows)


def test_frozen_model_spec_names_d18_decomposition_and_small_n_guard():
    text = (Path(__file__).resolve().parents[1] / "analysis" / "model_spec.md").read_text()
    assert "direct key" in text.lower() and "primary" in text.lower()
    assert "E(C1–C16)" in text
    assert "exploratory" in text.lower()
    assert "N=30" in text
    assert "0.90" in text and "0.30" in text and "rank 15" in text.lower()
    assert "tool, target, operation, arguments" in text
    assert "invalid_action" in text
    assert "evasion_key" in text and "ambiguous" in text
    assert "eight independent" in text.lower()
    assert "JCASE-<UUIDv4>" in text and "JUDGE-<UUIDv4>" in text
    assert "16 × 5 × 3" in text
    assert "lib.blocks.build_deep_structures" in text
