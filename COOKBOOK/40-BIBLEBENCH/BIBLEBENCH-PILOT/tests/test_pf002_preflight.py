from __future__ import annotations

import json
from pathlib import Path


PACKAGE_ROOT = Path(__file__).parents[1]
PREFLIGHT_ROOT = PACKAGE_ROOT / "preflight"
PROPOSAL = PREFLIGHT_ROOT / "pf002-three-model-proposal.json"
EVIDENCE = PREFLIGHT_ROOT / "verified-model-evidence.json"
CONSISTENCY = PREFLIGHT_ROOT / "pf002-preflight-consistency.json"
AUTH_REQUEST = PREFLIGHT_ROOT / "PF002-OWNER-AUTHORIZATION-REQUEST.md"
CHECKPOINT_JSON = PACKAGE_ROOT / "pilot-cost-estimate.json"
CHECKPOINT_MD = PACKAGE_ROOT / "PILOT-COST-CHECKPOINT.md"


def test_owner_ready_preflight_artifact_inventory_exists() -> None:
    expected = (
        PROPOSAL,
        EVIDENCE,
        CONSISTENCY,
        AUTH_REQUEST,
        CHECKPOINT_JSON,
        CHECKPOINT_MD,
    )
    assert all(path.is_file() for path in expected)


def test_preflight_is_exactly_pf002_and_non_authorizing() -> None:
    proposal = json.loads(PROPOSAL.read_text(encoding="utf-8"))
    assert proposal["provenance"] == "PROPOSAL_ONLY"
    assert proposal["status"] == "PROPOSAL_ONLY"
    assert proposal["authorized"] is False
    assert proposal["geometry"] == {
        "actor_count": 3,
        "capability_twins": False,
        "episode_count": 48,
        "logical_call_count": 288,
        "primary_count": 144,
        "probe_count": 144,
    }
    assert proposal["cue"] == "C1"
    assert proposal["fallback_enabled"] is False
    assert proposal["budget"]["forecast_usd"] <= 3
    assert proposal["budget"]["hard_cap_usd"] == 5
    assert proposal["budget"]["not_to_exceed_usd"] == 5


def test_active_checkpoint_contains_no_superseded_geometry() -> None:
    text = CHECKPOINT_MD.read_text(encoding="utf-8")
    forbidden = ("four-model", "1,344", "1,356", "C0/C1/C2", "Mistral")
    assert not any(value.casefold() in text.casefold() for value in forbidden)
    assert "288 logical calls" in text
    assert "PROPOSAL_ONLY" in text
    assert "$5.00" in text
