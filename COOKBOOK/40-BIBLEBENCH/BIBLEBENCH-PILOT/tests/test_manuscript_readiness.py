from __future__ import annotations

from collections import Counter
from pathlib import Path
import re


PACKAGE_ROOT = Path(__file__).parents[1]
BIBLEBENCH_ROOT = PACKAGE_ROOT.parent
PAPER_ROOT = BIBLEBENCH_ROOT / "BIBLEBENCH-PAPER"
MANUSCRIPT_PATH = PAPER_ROOT / "manuscript.md"
REFERENCES_PATH = PAPER_ROOT / "references.bib"
SOURCE_VERIFICATION_PATH = PAPER_ROOT / "SOURCE-VERIFICATION.md"

REQUIRED_SECTIONS = (
    "Abstract",
    "Introduction",
    "Related Work",
    "Construct and Theological Frame",
    "Benchmark Design",
    "MVP Protocol",
    "Planned Analysis",
    "Ethics",
    "Limitations",
    "Results",
    "Discussion",
)


def _bib_entries() -> list[tuple[str, str]]:
    bibliography = REFERENCES_PATH.read_text(encoding="utf-8")
    starts = list(re.finditer(r"(?m)^@([A-Za-z]+)\{([A-Za-z][A-Za-z0-9_-]+),", bibliography))
    entries: list[tuple[str, str]] = []
    for index, match in enumerate(starts):
        end = starts[index + 1].start() if index + 1 < len(starts) else len(bibliography)
        entries.append((match.group(2), bibliography[match.start() : end]))
    return entries


def test_submission_sections_and_single_results_sentinel() -> None:
    manuscript = MANUSCRIPT_PATH.read_text(encoding="utf-8")
    headings = {
        re.sub(r"^\d+\.?\s*", "", heading).strip()
        for heading in re.findall(r"(?m)^##\s+(.+)$", manuscript)
    }
    assert set(REQUIRED_SECTIONS) <= headings
    assert manuscript.count("PENDING_EMPIRICAL_RUN") == 1
    results = re.search(
        r"(?ms)^##\s+(?:\d+\.?\s*)?Results\s*$\n(.*?)(?=^##\s+|\Z)", manuscript
    )
    assert results is not None
    assert results.group(1).count("PENDING_EMPIRICAL_RUN") == 1


def test_all_pandoc_citations_resolve_and_bibtex_keys_are_unique() -> None:
    manuscript = MANUSCRIPT_PATH.read_text(encoding="utf-8")
    cited: set[str] = set()
    for group in re.findall(r"\[(@[^\]]+)\]", manuscript):
        cited.update(re.findall(r"@([A-Za-z][A-Za-z0-9_-]+)", group))

    entries = _bib_entries()
    keys = [key for key, _ in entries]
    duplicates = [key for key, count in Counter(keys).items() if count > 1]
    assert not duplicates
    assert cited
    assert cited <= set(keys)


def test_external_references_have_stable_identifiers_and_local_sources_are_distinct() -> None:
    entries = _bib_entries()
    assert entries
    for key, entry in entries:
        if re.search(r"(?i)keywords\s*=\s*\{[^}]*local[-_ ]provenance", entry):
            assert "Local path:" in entry, key
            continue
        assert re.search(r"(?im)^\s*(doi|url|eprint)\s*=", entry), key

    verification = SOURCE_VERIFICATION_PATH.read_text(encoding="utf-8")
    external_keys = {
        key
        for key, entry in entries
        if not re.search(r"(?i)keywords\s*=\s*\{[^}]*local[-_ ]provenance", entry)
    }
    for key in external_keys:
        assert f"`{key}`" in verification, key


def test_pf002_mvp_geometry_and_claim_ceiling_are_explicit() -> None:
    manuscript = MANUSCRIPT_PATH.read_text(encoding="utf-8")
    normalized = manuscript.lower()
    assert "exactly three inexpensive general-purpose models" in normalized
    assert "48 episodes" in normalized
    assert "one c1 primary and one matched probe" in normalized
    assert "288 logical calls" in normalized
    for excluded in (
        "rankings",
        "composites",
        "best-model",
        "cue-effect",
        "capability-adjusted",
        "family-level",
        "christian-consensus",
        "performance claims",
    ):
        assert excluded in normalized


def test_discussion_has_required_pre_empirical_scaffolds() -> None:
    manuscript = MANUSCRIPT_PATH.read_text(encoding="utf-8")
    discussion = re.search(
        r"(?ms)^##\s+(?:\d+\.?\s*)?Discussion\s*$\n(.*?)(?=^##\s+|\Z)", manuscript
    )
    assert discussion is not None
    for scaffold in (
        "Findings to interpret after the run",
        "Alternative explanations",
        "Theological scope",
        "Future multi-judge validation",
    ):
        assert scaffold in discussion.group(1)
