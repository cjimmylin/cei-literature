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
LIMITATIONS_PATH = PAPER_ROOT / "limitations-register.md"

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
