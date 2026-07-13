from __future__ import annotations

from pathlib import Path
import hashlib
import re
import subprocess
import sys

from pypdf import PdfReader
import yaml


PACKAGE_ROOT = Path(__file__).parents[1]
BIBLEBENCH_ROOT = PACKAGE_ROOT.parent
PAPER_ROOT = BIBLEBENCH_ROOT / "BIBLEBENCH-PAPER"
REGISTRY = PAPER_ROOT / "reports" / "report-registry.yaml"
BUILDER = PAPER_ROOT / "tools" / "build_design_reports.py"
OUTPUT = PAPER_ROOT / "output" / "design-reports"
QA = OUTPUT / "QA.md"

EXPECTED = {
    "01-biblebench-consolidated-design-and-methods.pdf",
    "02-fruitbench-design-report.pdf",
    "03-corinthlove-design-report.pdf",
    "04-10cbench-30-design-atlas.pdf",
    "05-sermonmount-design-report.pdf",
    "06-shared-episode-protocol-and-custody.pdf",
    "07-human-adjudication-handbook.pdf",
    "08-reproducibility-ethics-and-data-card.pdf",
    "09-analysis-tables-figures-and-claims-boundary.pdf",
}


def _registry() -> dict:
    return yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))


def _pdf_text(path: Path) -> tuple[PdfReader, str]:
    reader = PdfReader(path)
    return reader, "\n".join(page.extract_text() or "" for page in reader.pages)


def test_registry_has_exact_inventory_and_resolvable_sources() -> None:
    registry = _registry()
    reports = registry["reports"]
    assert registry["status"] == "PRE-EMPIRICAL DESIGN REPORT"
    assert {report["filename"] for report in reports} == EXPECTED
    assert len(reports) == 9
    for report in reports:
        assert report["title"]
        assert report["required_phrases"]
        for relative in report["sources"]:
            path = BIBLEBENCH_ROOT / relative
            assert path.is_file(), path
            assert path.stat().st_size > 0


def test_tencommandments_source_has_all_thirty_unique_design_ids() -> None:
    source = (BIBLEBENCH_ROOT / "output" / "10cbench-30-designs-overview.md").read_text(encoding="utf-8")
    identifiers = re.findall(r"^# (\d{2}[ABC]) ([A-Z]+) - ", source, flags=re.MULTILINE)
    assert len(identifiers) == 30
    assert len(set(identifiers)) == 30
    assert {suffix for _, suffix in identifiers} >= {"SOVEREIGN", "TABLETS", "PREFACE"}


def test_builder_generates_nine_searchable_pre_empirical_pdfs() -> None:
    subprocess.run([sys.executable, str(BUILDER)], check=True, cwd=BIBLEBENCH_ROOT)
    assert {path.name for path in OUTPUT.glob("*.pdf")} == EXPECTED
    for path in sorted(OUTPUT.glob("*.pdf")):
        reader, text = _pdf_text(path)
        assert reader.pages
        assert all((page.extract_text() or "").strip() for page in reader.pages)
        assert "PRE-EMPIRICAL DESIGN REPORT" in text
        assert "Jimmy Lin" in text
        assert "Page " in text
        assert "turn" + "0search" not in text
        assert "[@" not in text
        assert "TBD" not in text
        assert "TODO" not in text
        metadata = reader.metadata
        assert metadata.author == "Jimmy Lin"
        assert "pre-empirical" in (metadata.subject or "").lower()
        assert metadata.creator == "BibleBench design-report builder"


def test_tencommandments_pdf_contains_all_thirty_design_ids() -> None:
    _, text = _pdf_text(OUTPUT / "04-10cbench-30-design-atlas.pdf")
    for number in range(1, 11):
        for suffix in "ABC":
            assert f"{number:02d}{suffix}" in text
    assert "MVP module boundary and executable episodes" in text
    assert "broadly evangelical-Protestant" in text
    assert "Passage anchors" in text
    assert "Prohibited actions" in text
    assert "Deficient pole" in text
    assert "Counterfeit pole" in text
    assert "Provenance:" in text


def test_shared_protocol_uses_pf002_custody_geometry_only() -> None:
    _, text = _pdf_text(OUTPUT / "06-shared-episode-protocol-and-custody.pdf")
    text = re.sub(r"\s+", " ", text)
    assert "288 logical calls" in text
    assert "one C1 primary plus its matched probe" in text
    assert "C0/C2 contrasts" in text
    assert "remain deferred" in text
    assert "144 pair-scoped rows" not in text
    assert "active C0/C1/C2 custody" not in text


def test_report_build_is_byte_deterministic() -> None:
    subprocess.run([sys.executable, str(BUILDER)], check=True, cwd=BIBLEBENCH_ROOT)
    first = {path.name: hashlib.sha256(path.read_bytes()).hexdigest() for path in OUTPUT.glob("*.pdf")}
    subprocess.run([sys.executable, str(BUILDER)], check=True, cwd=BIBLEBENCH_ROOT)
    second = {path.name: hashlib.sha256(path.read_bytes()).hexdigest() for path in OUTPUT.glob("*.pdf")}
    assert first == second


def test_qa_registers_every_delivered_pdf_hash() -> None:
    qa = QA.read_text(encoding="utf-8")
    for path in OUTPUT.glob("*.pdf"):
        assert hashlib.sha256(path.read_bytes()).hexdigest() in qa
    assert "All 86 pages were rendered with Poppler" in qa


def test_analysis_report_preserves_pre_run_claim_boundary() -> None:
    _, text = _pdf_text(OUTPUT / "09-analysis-tables-figures-and-claims-boundary.pdf")
    assert "PENDING_EMPIRICAL_RUN" in text
    assert "no leaderboard" in text.lower()
    assert "p-value" in text.lower()
    assert "capability-adjusted" in text.lower()
