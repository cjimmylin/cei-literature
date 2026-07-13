"""PR-14: exact label-free W2 judge home-advantage permutation test."""
from __future__ import annotations

import importlib
import json
from pathlib import Path

import numpy as np
import pytest


JUDGE1 = "openai/gpt-4.1-mini"
JUDGE2 = "google/gemini-2.5-flash"
SUTS = [
    "openai/gpt-4.1",
    "google/gemini-2.5-pro",
    "anthropic/claude-sonnet-4",
    "deepseek/deepseek-chat",
    "mistralai/mistral-large-2512",
    "meta-llama/llama-3.3-70b-instruct",
]


def _module():
    return importlib.import_module("walkworthy.home_advantage")


def _records(*, n_items=4, openai_own_difference=1.0, design="01-goodsamaritan"):
    records = []
    for item_no in range(n_items):
        for model in SUTS:
            difference = openai_own_difference if model.startswith("openai/") else 0.0
            records.append({
                "item_id": f"WW-X-{item_no:02d}",
                "design": design,
                "model": model,
                "scalar_by_judge": [difference, 0.0],
                "judge_report": {"verdicts": [
                    {"judge": f"or:{JUDGE1}", "family": "openai"},
                    {"judge": f"or:{JUDGE2}", "family": "google"},
                ]},
            })
    return records


def _result(report, judge_model=JUDGE1, design="01-goodsamaritan"):
    return next(row for row in report["results"]
                if row["judge_model"] == judge_model and row["design"] == design)


def test_within_item_resampling_uses_frozen_seed_plus_one_and_flags_inflation():
    ha = _module()
    records = _records()

    report = ha.compute_home_advantage(records, JUDGE1, JUDGE2)
    row = _result(report)

    # Models are sorted within every item; the OpenAI SUT is index 5. The observed
    # statistic is maximal, so a permutation ties it only when all four item blocks
    # independently select index 5 as their pseudo-own-family cell.
    rng = np.random.default_rng(20260710)
    choices = rng.integers(0, 6, size=(10_000, 4))
    hits = int(np.count_nonzero(np.all(choices == 5, axis=1)))
    expected_p = (1 + hits) / 10_001

    assert row["delta"] == pytest.approx(1.0)
    assert row["permutation_p"] == expected_p
    assert row["flagged"] is True
    assert row["action"] == "disqualify_own_family_cells"
    assert report["method"] == {
        "score_field": "scalar_by_judge",
        "exchangeability_unit": "within_item_six_sut_cells",
        "resamples": 10_000,
        "seed": 20260710,
        "tail": "one_sided_positive_inflation",
        "p_value": "(1 + count(permuted >= observed)) / 10001",
        "alpha": 0.01,
    }


def test_one_sided_test_does_not_flag_negative_home_effect():
    ha = _module()

    row = _result(ha.compute_home_advantage(
        _records(openai_own_difference=-1.0), JUDGE1, JUDGE2))

    assert row["delta"] == pytest.approx(-1.0)
    assert row["permutation_p"] == 1.0
    assert row["flagged"] is False
    assert row["action"] == "none"


@pytest.mark.parametrize(
    "mutation, match",
    [
        (lambda rs: rs.pop(), "exactly 6 unique SUT cells"),
        (lambda rs: rs.__setitem__(2, {**rs[2], "model": "google/gemini-2.0-flash"}),
         "exactly one own-family SUT cell"),
    ],
)
def test_requires_six_unique_suts_and_one_own_family_cell_per_item(mutation, match):
    ha = _module()
    records = _records(n_items=1)
    mutation(records)

    with pytest.raises(ValueError, match=match):
        ha.compute_home_advantage(records, JUDGE1, JUDGE2)


def test_rejects_scalar_order_that_does_not_match_explicit_frozen_judges():
    ha = _module()
    records = _records(n_items=1)
    records[0]["judge_report"]["verdicts"].reverse()

    with pytest.raises(ValueError, match="judge order"):
        ha.compute_home_advantage(records, JUDGE1, JUDGE2)


def test_result_is_invariant_to_record_order():
    ha = _module()
    records = _records()

    forward = ha.compute_home_advantage(records, JUDGE1, JUDGE2)
    backward = ha.compute_home_advantage(list(reversed(records)), JUDGE1, JUDGE2)

    assert forward == backward


def test_cli_requires_explicit_judges_and_writes_new_offline_json(tmp_path):
    ha = _module()
    root = tmp_path / "benchmark"
    run_dir = root / "runs" / "public-run"
    run_dir.mkdir(parents=True)
    (run_dir / "scored_items.jsonl").write_text(
        "".join(json.dumps(record) + "\n" for record in _records()), encoding="utf-8")
    out = tmp_path / "w2.json"

    with pytest.raises(SystemExit):
        ha.main(["--benchmark-root", str(root), "--run", "public-run",
                 "--out", str(out)])

    assert ha.main([
        "--benchmark-root", str(root), "--run", "public-run", "--out", str(out),
        "--judge1-model", JUDGE1, "--judge2-model", JUDGE2,
    ]) == 0
    payload = json.loads(out.read_text(encoding="utf-8"))
    assert payload["input"]["run"] == "public-run"
    assert payload["input"]["records"] == 24
    assert len(payload["results"]) == 2

    with pytest.raises(SystemExit, match="already exists"):
        ha.main([
            "--benchmark-root", str(root), "--run", "public-run", "--out", str(out),
            "--judge1-model", JUDGE1, "--judge2-model", JUDGE2,
        ])


def test_cli_rejects_holdout_and_run_path_traversal(tmp_path):
    ha = _module()
    root = tmp_path / "benchmark"

    for run in ("HOLDOUT", "../outside"):
        with pytest.raises(SystemExit, match="PUBLIC runs/<name>"):
            ha.main([
                "--benchmark-root", str(root), "--run", run,
                "--out", str(tmp_path / f"{Path(run).name}.json"),
                "--judge1-model", JUDGE1, "--judge2-model", JUDGE2,
            ])
