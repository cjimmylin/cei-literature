from __future__ import annotations

import sys
from pathlib import Path

import pytest


BANK = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BANK / "lib"))

import split_hygiene  # noqa: E402


def row(item_id: str, split: str, phrase: str) -> dict:
    affordances = [
        {
            "tool": f"tool-{index}", "target": f"target-{index}",
            "operation": f"operation-{index}",
            "arguments": {"message": f"{phrase} argument {index}"},
            "description": f"{phrase} description {index}",
        }
        for index in range(4)
    ]
    return {
        "id": item_id,
        "split": split,
        "template_family": "family-a",
        "multiturn_script": {
            stage: [f"{phrase} {index} turn {turn}" for turn in range(
                3 if stage == "stage_3" else 1
            )]
            for index, stage in enumerate(split_hygiene.STAGES, 1)
        },
        "tools": [
            {"name": f"tool-{index}", "description": f"{phrase} tool {index}"}
            for index in range(4)
        ],
        "affordances": affordances,
        "visible_consequences": [f"{phrase} consequence state"],
    }


def hidden(item_id: str, skin: str, region: str, phrase: str) -> dict:
    paths = {f"path-{index}": {"C1": 1} for index in range(4)}
    branches = {}
    for branch_id in [*paths, "evasion"]:
        branches[branch_id] = {
            "turns": [f"{phrase} reaction {branch_id}"],
            "public_branch_state": {"artifact": f"{phrase} branch artifact"},
            "repair_affordances": [
                {
                    "tool": f"repair-{index}", "target": f"repair-target-{index}",
                    "operation": f"repair-operation-{index}",
                    "arguments": {"value": f"{phrase} repair {index}"},
                    "description": f"{phrase} repair description {index}",
                }
                for index in range(2)
            ],
            "closeout_affordances": [{
                "tool": "close", "target": "close-target",
                "operation": "close-operation",
                "arguments": {"value": f"{phrase} close"},
                "description": f"{phrase} close description",
            }],
        }
    return {
        "skin_id": skin, "parameter_region_id": region,
        "path_keys": paths, "reaction_table": branches,
    }


def test_clean_splits_require_disjoint_text_skins_and_parameter_regions():
    public = [row("PUB-1", "public", "orchard public alpha")]
    private = [row("PRI-1", "private", "harbor sealed omega")]
    sidecar = {
        "PUB-1": hidden("PUB-1", "skin-public", "region-public", "orchard public alpha"),
        "PRI-1": hidden("PRI-1", "skin-private", "region-private", "harbor sealed omega"),
    }
    report = split_hygiene.audit(public, private, sidecar, threshold=0.25)
    assert report["violations"] == []
    assert report["counts"] == {"public": 1, "private": 1}
    split_hygiene.assert_clean(report)


def test_exact_or_near_copy_across_splits_fails_loudly():
    public = [row("PUB-1", "public", "identical four token core phrase")]
    private = [row("PRI-1", "private", "identical four token core phrase")]
    sidecar = {
        "PUB-1": hidden("PUB-1", "a", "a", "identical four token core phrase"),
        "PRI-1": hidden("PRI-1", "b", "b", "identical four token core phrase"),
    }
    report = split_hygiene.audit(public, private, sidecar)
    assert report["violations"]
    with pytest.raises(AssertionError, match="split hygiene"):
        split_hygiene.assert_clean(report)


def test_skin_or_parameter_region_reuse_is_a_violation():
    public = [row("PUB-1", "public", "public phrasing")]
    private = [row("PRI-1", "private", "private phrasing")]
    sidecar = {
        "PUB-1": hidden("PUB-1", "same", "public", "public phrasing"),
        "PRI-1": hidden("PRI-1", "same", "private", "private phrasing"),
    }
    report = split_hygiene.audit(public, private, sidecar)
    assert any(v["kind"] == "skin_overlap" for v in report["violations"])


def test_real_bank_full_future_surface_has_all_fields_and_zero_violations():
    from generator import build_bank

    bank = build_bank()
    report = bank.split_audit
    assert report["comparison_scope"] == "all-public-x-all-private"
    assert report["comparisons"] == 30 * 600
    assert set(report["future_visible_fields"]) == set(
        split_hygiene.FUTURE_VISIBLE_FIELDS
    )
    assert report["max_containment"] < 0.25
    assert report["violations"] == []
