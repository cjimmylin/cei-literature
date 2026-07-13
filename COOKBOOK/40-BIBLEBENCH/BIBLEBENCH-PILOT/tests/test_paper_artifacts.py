from __future__ import annotations

from pathlib import Path
import re

import yaml


PACKAGE_ROOT = Path(__file__).parents[1]
BIBLEBENCH_ROOT = PACKAGE_ROOT.parent
PAPER_ROOT = BIBLEBENCH_ROOT / "BIBLEBENCH-PAPER"
MANUSCRIPT_PATH = PAPER_ROOT / "manuscript.md"
CLAIMS_PATH = PAPER_ROOT / "claims-registry.yaml"
REFERENCES_PATH = PAPER_ROOT / "references.bib"
SOURCE_VERIFICATION_PATH = PAPER_ROOT / "SOURCE-VERIFICATION.md"
LIMITATIONS_PATH = PAPER_ROOT / "limitations-register.md"
APPENDIX_PATHS = (
    PAPER_ROOT / "appendix-reproducibility.md",
    PAPER_ROOT / "appendix-ethics.md",
    PAPER_ROOT / "appendix-data-card.md",
)

ALLOWED_CLAIM_TYPES = {
    "DESIGN_CLAIM",
    "ENGINEERING_CLAIM",
    "PROVISIONAL_THEOLOGICAL_JUDGMENT",
    "EMPIRICAL_CLAIM_PENDING",
    "EMPIRICAL_CLAIM",
}


def test_paper_package_exists_and_remains_pre_empirical() -> None:
    for path in (MANUSCRIPT_PATH, CLAIMS_PATH, REFERENCES_PATH, LIMITATIONS_PATH):
        assert path.is_file(), path

    manuscript = MANUSCRIPT_PATH.read_text(encoding="utf-8")
    registry = yaml.safe_load(CLAIMS_PATH.read_text(encoding="utf-8"))

    assert manuscript.count("PENDING_EMPIRICAL_RUN") == 1
    assert registry["document_status"] == "pre_empirical_design_and_methods"
    assert registry["empirical_claim_count"] == 0
    assert all(claim["type"] in ALLOWED_CLAIM_TYPES for claim in registry["claims"])
    assert all(claim["type"] != "EMPIRICAL_CLAIM" for claim in registry["claims"])


def test_every_registered_claim_is_used_and_has_local_support() -> None:
    manuscript = MANUSCRIPT_PATH.read_text(encoding="utf-8")
    registry = yaml.safe_load(CLAIMS_PATH.read_text(encoding="utf-8"))
    claims = registry["claims"]
    claim_ids = {claim["id"] for claim in claims}
    assert len(claim_ids) == len(claims)

    cited_claim_ids: set[str] = set()
    for group in re.findall(r"\[((?:[DEPX]\d{3})(?:; [DEPX]\d{3})*)\]", manuscript):
        cited_claim_ids.update(group.split("; "))
    assert cited_claim_ids == claim_ids

    for claim in claims:
        for support in claim.get("support", []):
            if "path" in support:
                assert (BIBLEBENCH_ROOT.parents[1] / support["path"]).is_file(), (
                    claim["id"],
                    support["path"],
                )
            else:
                assert {"command", "cwd", "observed_result"} <= set(support), claim["id"]


def test_all_manuscript_citation_keys_resolve_locally() -> None:
    manuscript = MANUSCRIPT_PATH.read_text(encoding="utf-8")
    bibliography = REFERENCES_PATH.read_text(encoding="utf-8")
    cited_keys = set(re.findall(r"@([A-Za-z][A-Za-z0-9_-]+)", manuscript))
    bibliography_keys = set(
        re.findall(r"@[A-Za-z]+\{([A-Za-z][A-Za-z0-9_-]+),", bibliography)
    )
    assert cited_keys
    assert cited_keys <= bibliography_keys


def test_passage_and_confessional_frame_have_verified_external_support() -> None:
    manuscript = MANUSCRIPT_PATH.read_text(encoding="utf-8")
    bibliography = REFERENCES_PATH.read_text(encoding="utf-8")
    verification = SOURCE_VERIFICATION_PATH.read_text(encoding="utf-8")

    expected_sources = {
        "desilvaGalatians2018": (
            "9780802830555",
            "https://www.eerdmans.com/9780802830555/the-letter-to-the-galatians/",
        ),
        "thiseltonCorinthians2000": (
            "9780802824493",
            "https://www.eerdmans.com/9780802824493/the-first-epistle-to-the-corinthians/",
        ),
        "durhamExodus2015": (
            "9780310522270",
            "https://zondervanacademic.com/products/exodus-volume-3",
        ),
        "millerTenCommandments2009": (
            "9780664264758",
            "https://www.wjkbooks.com/bookproduct/0664264751-the-ten-commandments/",
        ),
        "turnerMatthew2008": (
            "9780801026843",
            "https://bakeracademic.com/p/Matthew-David-L-Turner/40386",
        ),
        "opcWestminsterStandards": (
            "Westminster Confession of Faith",
            "https://www.opc.org/standards.html",
        ),
    }

    for key, (stable_id, official_url) in expected_sources.items():
        assert f"@{key}" in manuscript, key
        assert re.search(rf"@[A-Za-z]+\{{{re.escape(key)},", bibliography), key
        assert stable_id in bibliography, (key, stable_id)
        assert key in verification, key
        assert official_url in verification, (key, official_url)

    assert "FruitBench's Galatians 5:13–26 anchor [@desilvaGalatians2018]" in manuscript
    assert "CORINTHLOVE's 1 Corinthians 13 context [@thiseltonCorinthians2000]" in manuscript
    assert "10CBench's Exodus 20/Deuteronomy 5 anchor [@durhamExodus2015; @millerTenCommandments2009]" in manuscript
    assert "SermonMount's Matthew 5–7 frame [@turnerMatthew2008]" in manuscript
    assert "[@opcWestminsterStandards]" in manuscript


def test_appendix_contracts_are_current_pre_empirical_and_noncontaminating() -> None:
    required_markers = {
        "appendix-reproducibility.md": (
            "48 episodes",
            "288 logical calls",
            "No live model calls",
        ),
        "appendix-ethics.md": (
            "single-expert provisional gold",
            "No Christian consensus",
            "No real people",
        ),
        "appendix-data-card.md": (
            "34 common-life",
            "14 Christian-facing",
            "No model outputs",
        ),
    }
    prohibited = (
        "private repeat mapping",
        "repeat membership",
        "suggested judgment",
        "suggested rationale",
        "recommended label",
    )

    for path in APPENDIX_PATHS:
        assert path.is_file(), path
        text = path.read_text(encoding="utf-8")
        assert "Current status: pre-empirical" in text
        for marker in required_markers[path.name]:
            assert marker in text, (path.name, marker)
        lowered = text.lower()
        for phrase in prohibited:
            assert phrase not in lowered, (path.name, phrase)
