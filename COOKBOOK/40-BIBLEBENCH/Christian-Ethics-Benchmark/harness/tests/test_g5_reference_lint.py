"""Directed G5 pre-gate lint (Fable review §4(d), no live scoring)."""
from pathlib import Path

from walkworthy.g5_reference_lint import lint_reference_files, lint_text


def test_guilt_lint_flags_unnegated_guilt_but_accepts_explicit_negation():
    bad = lint_text(
        "06", "WW-06-X", [
            ("no-dilemma", "Choose the truthful path. You should repent for choosing it."),
            ("dilemma", "Choose the other path and carry its cost."),
        ])
    good = lint_text(
        "06", "WW-06-X", [
            ("no-dilemma", "Choose the truthful path and carry the cost, not guilt."),
            ("dilemma", "Choose the other path and carry its cost."),
        ])

    assert any(f["check"] == "FA-1" for f in bad["failures"])
    assert not any(f["check"] == "FA-1" for f in good["failures"])


def test_directed_pre_gate_lint_passes_both_final_reference_drafts(benchmark_root):
    report = lint_reference_files(
        Path(benchmark_root) / "00-PORTFOLIO/20260712-G5-06-references-DRAFT.md",
        Path(benchmark_root) / "00-PORTFOLIO/20260712-G5-09-references-DRAFT.md",
        Path(benchmark_root) / "DESIGNS/09-doubleedge-seeds.md",
    )

    assert report["designs"]["06"]["pair_count"] == 10
    assert report["designs"]["09"]["pair_count"] == 10
    assert report["failures"] == []
    assert report["directed"]["09-D01-rendered-facts"] == "PASS"
    assert report["directed"]["06-K03-split-kind"] == "verdict"
    assert report["directed"]["06-D01-max-ratio"] <= 1.10
    assert report["directed"]["06-L03-max-ratio"] <= 1.10
