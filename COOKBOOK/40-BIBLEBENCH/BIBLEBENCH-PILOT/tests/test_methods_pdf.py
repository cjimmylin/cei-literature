from __future__ import annotations

from pathlib import Path
import hashlib
import re
import subprocess
import sys

from pypdf import PdfReader


PACKAGE_ROOT = Path(__file__).parents[1]
BIBLEBENCH_ROOT = PACKAGE_ROOT.parent
PAPER_ROOT = BIBLEBENCH_ROOT / "BIBLEBENCH-PAPER"
BUILDER = PAPER_ROOT / "tools" / "build_methods_pdf.py"
OUTPUT = PAPER_ROOT / "output" / "pdf" / "biblebench-methods-prerelease.pdf"
QA = PAPER_ROOT / "output" / "pdf" / "QA.md"


def test_methods_pdf_builds_as_a_clearly_pre_empirical_artifact() -> None:
    subprocess.run([sys.executable, str(BUILDER)], check=True, cwd=BIBLEBENCH_ROOT)

    reader = PdfReader(OUTPUT)
    text = "\n".join(page.extract_text() or "" for page in reader.pages)
    metadata = reader.metadata

    assert len(reader.pages) >= 8
    assert metadata.title == (
        "BibleBench: A Passage-Preserving Design for Observable Ethical and "
        "Biblical Evaluation of Language Models"
    )
    assert metadata.author == "Jimmy Lin"
    assert "prerelease" in (metadata.subject or "").lower()
    assert "no live-model evidence" in (metadata.subject or "").lower()
    assert "Abstract" in text
    assert "Planned evaluation" in text
    assert "Local references" in text
    assert text.count("PENDING_EMPIRICAL_RUN") == 1
    assert "Proposal only; $0.00 authorized" in text


def test_methods_pdf_source_and_output_paths_are_inside_the_paper_package() -> None:
    assert BUILDER.is_file()
    assert OUTPUT.parent == PAPER_ROOT / "output" / "pdf"


def test_methods_pdf_resolves_citations_and_renders_bibliography() -> None:
    subprocess.run([sys.executable, str(BUILDER)], check=True, cwd=BIBLEBENCH_ROOT)

    reader = PdfReader(OUTPUT)
    text = "\n".join(page.extract_text() or "" for page in reader.pages)
    normalized = re.sub(r"\s+", " ", text)

    assert re.search(r"\[@[A-Za-z][A-Za-z0-9]*", text) is None
    assert "Bibliography" in normalized
    assert "Liu et al., 2024" in normalized
    assert "Pan et al., 2023" in normalized

    required_passage_and_confessional_sources = (
        ("deSilva, 2018", "The Letter to the Galatians"),
        ("Thiselton, 2000", "The First Epistle to the Corinthians"),
        ("Durham, 2015", "Exodus, Volume 3"),
        ("Miller, 2009", "The Ten Commandments"),
        ("Turner, 2008", "Matthew"),
        ("Orthodox Presbyterian Church, n.d.", "Westminster Confession of Faith"),
    )
    for inline_label, bibliography_marker in required_passage_and_confessional_sources:
        assert inline_label in normalized
        assert bibliography_marker in normalized

    local_design_sources = (
        ("BibleBench Project, 2026a", "BibleBench Project (2026a). BibleBench Shared Engine"),
        ("BibleBench Project, 2026b", "BibleBench Project (2026b). BibleBench 42-Core Selection"),
        ("BibleBench Project, 2026c", "BibleBench Project (2026c). BibleBench Parallel Paper-Readiness"),
    )
    for inline_label, bibliography_marker in local_design_sources:
        assert inline_label in normalized
        assert bibliography_marker in normalized


def test_methods_pdf_qa_registers_the_delivered_file_hash() -> None:
    digest = hashlib.sha256(OUTPUT.read_bytes()).hexdigest()

    assert digest in QA.read_text(encoding="utf-8")
