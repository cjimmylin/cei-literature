from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import urlparse


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


def test_evidence_registry_is_public_first_party_and_matches_proposal() -> None:
    evidence = json.loads(EVIDENCE.read_text(encoding="utf-8"))
    proposal = json.loads(PROPOSAL.read_text(encoding="utf-8"))
    assert evidence["classification"] == "PUBLIC_DOCUMENTATION_ONLY"
    assert evidence["credentials_accessed"] is False
    assert evidence["provider_calls_made"] == 0
    assert evidence["spend_usd"] == 0
    evidence_by_alias = {row["actor_alias"]: row for row in evidence["actors"]}
    assert set(evidence_by_alias) == {"actor-alpha", "actor-beta", "actor-gamma"}
    allowed_hosts = {
        "developers.openai.com",
        "platform.openai.com",
        "ai.google.dev",
        "platform.claude.com",
        "docs.anthropic.com",
    }
    for actor in proposal["actors"]:
        row = evidence_by_alias[actor["actor_alias"]]
        assert row["provider"] == actor["provider"]
        assert row["model_id"] == actor["model_id"]
        assert row["route_id"] == actor["route"]["route_id"]
        assert row["input_usd_per_million_tokens"] == actor["price"]["input_usd"]
        assert row["output_usd_per_million_tokens"] == actor["price"]["output_usd"]
        assert {
            urlparse(url).hostname for url in row["official_sources"]
        } <= allowed_hosts


def test_preflight_builder_is_deterministic_and_offline(monkeypatch) -> None:
    import socket

    from biblebench_pilot.preflight import build_preflight_bundle

    def denied(*args, **kwargs):
        raise AssertionError("network access attempted")

    monkeypatch.setattr(socket, "socket", denied)
    first = build_preflight_bundle(PACKAGE_ROOT)
    second = build_preflight_bundle(PACKAGE_ROOT)
    assert first == second
    assert set(first) == {
        "pf002-three-model-proposal.json",
        "pf002-preflight-consistency.json",
        "PF002-OWNER-AUTHORIZATION-REQUEST.md",
        "pilot-cost-estimate.json",
        "PILOT-COST-CHECKPOINT.md",
    }


def test_preflight_builder_imports_no_transport_or_credentials() -> None:
    source = (PACKAGE_ROOT / "src/biblebench_pilot/preflight.py").read_text(
        encoding="utf-8"
    )
    forbidden = (
        "requests",
        "httpx",
        "urllib.request",
        "socket.create_connection",
        "OPENAI_API_KEY",
        "ANTHROPIC_API_KEY",
        "GOOGLE_API_KEY",
        "keyring",
    )
    assert not any(value in source for value in forbidden)
