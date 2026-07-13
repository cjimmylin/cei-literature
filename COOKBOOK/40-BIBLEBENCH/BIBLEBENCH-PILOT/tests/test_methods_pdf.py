from __future__ import annotations

from pathlib import Path
import hashlib
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


def test_methods_pdf_qa_registers_the_delivered_file_hash() -> None:
    digest = hashlib.sha256(OUTPUT.read_bytes()).hexdigest()

    assert digest in QA.read_text(encoding="utf-8")
