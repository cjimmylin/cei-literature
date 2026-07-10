"""RED: end-to-end mock dry-run over all 10 designs — parse -> execute -> refusal
-> judge -> score -> schema-validate -> aggregate -> gates -> artifacts."""
import json

from walkworthy.run import mock_dry_run


def test_mock_dry_run_all_designs(benchmark_root, tmp_path):
    summary = mock_dry_run(benchmark_root, out_dir=tmp_path, date_str="20260709",
                           max_items_per_design=4)
    # all 10 designs exercised
    assert len(summary["designs"]) == 10
    for d, ds in summary["designs"].items():
        assert ds["n_records"] > 0, f"{d}: no scored records"
        assert ds["schema_errors"] == 0, f"{d}: {ds['schema_errors']} schema errors"
        assert "refusal_accounting" in ds
        assert "judge_disagreement_rate" in ds
        assert "gates" in ds and ds["gates"], f"{d}: no gate results"

    # artifacts written
    assert (tmp_path / "manifest.json").exists()
    assert (tmp_path / "dry_run_report.md").exists()
    assert (tmp_path / "design_summaries.json").exists()

    # manifest carries the pinned capability battery + fixed seeds, IDs only
    manifest = json.loads((tmp_path / "manifest.json").read_text())
    assert len(manifest["capability_battery"]) == 6
    assert manifest["permutation_seeds"]
    assert all(i.startswith("WW-") for i in manifest["item_ids"])

    # top-line: zero schema errors across the whole run
    assert summary["total_schema_errors"] == 0
    assert summary["total_records"] > 0


def test_dry_run_report_mentions_capability_battery(benchmark_root, tmp_path):
    mock_dry_run(benchmark_root, out_dir=tmp_path, date_str="20260709",
                 max_items_per_design=2)
    report = (tmp_path / "dry_run_report.md").read_text()
    assert "MMLU-Pro" in report and "SWE-bench" in report
    assert "capability" in report.lower()
