"""Deterministic, offline construction of the PF-002 owner-review packet."""

from __future__ import annotations

from datetime import date
from decimal import Decimal
import hashlib
import json
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from .mvp_runner import load_proposal, validate_proposal_contract


GENERATOR_VERSION = "pf002-owner-ready-preflight-v1"
PROPOSAL_FIXTURE = Path("tests/fixtures/mvp-proposal-real-unauthorized.json")
EVIDENCE_PATH = Path("preflight/verified-model-evidence.json")
_ALLOWED_SOURCE_HOSTS = {
    "developers.openai.com",
    "platform.openai.com",
    "ai.google.dev",
    "platform.claude.com",
    "docs.anthropic.com",
}


def _pretty_json(value: dict[str, Any]) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True) + "\n").encode("utf-8")


def _read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if type(value) is not dict:
        raise ValueError(f"expected object: {path}")
    return value


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _validate_evidence(
    proposal: dict[str, Any], evidence: dict[str, Any]
) -> None:
    if evidence.get("classification") != "PUBLIC_DOCUMENTATION_ONLY":
        raise ValueError("official public evidence required")
    if (
        evidence.get("credentials_accessed") is not False
        or evidence.get("provider_calls_made") != 0
        or Decimal(str(evidence.get("spend_usd"))) != Decimal("0")
    ):
        raise ValueError("evidence provenance is not zero-spend")
    actors = evidence.get("actors")
    if type(actors) is not list:
        raise ValueError("invalid evidence actors")
    evidence_by_alias = {row.get("actor_alias"): row for row in actors}
    if set(evidence_by_alias) != {
        "actor-alpha",
        "actor-beta",
        "actor-gamma",
    } or len(evidence_by_alias) != len(actors):
        raise ValueError("evidence roster mismatch")
    for actor in proposal["actors"]:
        row = evidence_by_alias[actor["actor_alias"]]
        expected = {
            "provider": actor["provider"],
            "model_id": actor["model_id"],
            "route_id": actor["route"]["route_id"],
            "api_family": actor["route"]["api_family"],
            "input_usd_per_million_tokens": actor["price"]["input_usd"],
            "output_usd_per_million_tokens": actor["price"]["output_usd"],
            "context_window_tokens": actor["context_window_tokens"],
            "maximum_output_tokens": actor["maximum_supported_output_tokens"],
        }
        if any(row.get(key) != value for key, value in expected.items()):
            raise ValueError(f"evidence mismatch for {actor['actor_alias']}")
        sources = row.get("official_sources")
        if (
            type(sources) is not list
            or not sources
            or any(
                type(source) is not str
                or urlparse(source).scheme != "https"
                or urlparse(source).hostname not in _ALLOWED_SOURCE_HOSTS
                for source in sources
            )
        ):
            raise ValueError("non-official evidence source")
        if row.get("registered_adapter_controls") != {
            "max_output_tokens": 700,
            "temperature": 0,
        }:
            raise ValueError("adapter-control evidence mismatch")
        control_sources = row.get("control_evidence_sources")
        if (
            type(control_sources) is not list
            or not control_sources
            or any(
                type(source) is not str
                or urlparse(source).scheme != "https"
                or urlparse(source).hostname not in _ALLOWED_SOURCE_HOSTS
                for source in control_sources
            )
        ):
            raise ValueError("non-official adapter-control source")


def _checkpoint_payload(
    proposal: dict[str, Any], evidence: dict[str, Any], total: Decimal
) -> dict[str, Any]:
    evidence_by_alias = {row["actor_alias"]: row for row in evidence["actors"]}
    models = []
    for actor in proposal["actors"]:
        source = evidence_by_alias[actor["actor_alias"]]
        models.append(
            {
                "actor_alias": actor["actor_alias"],
                "api_family": actor["route"]["api_family"],
                "input_usd_per_million_tokens": actor["price"]["input_usd"],
                "max_input_tokens": actor["token_caps"]["max_input_tokens"],
                "max_output_tokens": actor["token_caps"]["max_output_tokens"],
                "model_id": actor["model_id"],
                "official_sources": source["official_sources"],
                "output_usd_per_million_tokens": actor["price"]["output_usd"],
                "provider": actor["provider"],
                "route_id": actor["route"]["route_id"],
                "route_worst_case_usd": actor["route_worst_case_usd"],
            }
        )
    return {
        "authorized": False,
        "calculated_worst_case_usd": float(total),
        "calls_made": 0,
        "cue": "C1",
        "estimate_version": "pf002-three-model-preflight-v1",
        "evidence_registry_sha256": _sha256(_pretty_json(evidence)),
        "expires_on": proposal["expires_on"],
        "forecast_limit_usd": 3,
        "forecast_usd": float(total),
        "geometry": {
            "actors": 3,
            "episodes": 48,
            "logical_calls": 288,
            "maximum_attempts_per_logical_call": 2,
            "primary_calls": 144,
            "probe_calls": 144,
        },
        "hard_nte_usd": 5,
        "models": models,
        "proposal_manifest_sha256": proposal["manifest_sha256"],
        "spend_usd": 0,
        "status": "PROPOSAL_ONLY",
        "stop_rules": [
            "Do not access credentials or construct transport without owner approval.",
            "Stop before any call if the exact manifest, roster, expiry, or NTE changes.",
            "Stop before forecast exceeds 3 USD or spend could exceed 5 USD.",
        ],
        "verified_on": evidence["verified_on"],
    }


def _consistency_payload(
    proposal: dict[str, Any],
    evidence: dict[str, Any],
    checkpoint: dict[str, Any],
) -> dict[str, Any]:
    return {
        "authorized": False,
        "budget": proposal["budget"],
        "checkpoint_sha256": _sha256(_pretty_json(checkpoint)),
        "classification": "PROPOSAL_ONLY",
        "credentials_accessed": False,
        "evidence_registry_sha256": _sha256(_pretty_json(evidence)),
        "generated_by": GENERATOR_VERSION,
        "geometry": proposal["geometry"],
        "proposal_manifest_sha256": proposal["manifest_sha256"],
        "provider_calls_made": 0,
        "spend_usd": 0,
        "verified_on": evidence["verified_on"],
    }


def _authorization_markdown(
    proposal: dict[str, Any],
    evidence: dict[str, Any],
    consistency: dict[str, Any],
) -> str:
    roster = "\n".join(
        "| {alias} | {provider} | `{model}` | `{route}` | "
        "${input_price:.2f} / ${output_price:.2f} | 4,096 input / 700 output |".format(
            alias=actor["actor_alias"],
            provider=actor["provider"],
            model=actor["model_id"],
            route=actor["route"]["route_id"],
            input_price=actor["price"]["input_usd"],
            output_price=actor["price"]["output_usd"],
        )
        for actor in proposal["actors"]
    )
    hashes = proposal["snapshot_hashes"]
    return f"""# PF-002 Owner Authorization Request

Status: `NOT_AUTHORIZED`

Owner: _blank_

Approval reference: _blank_

Authorization nonce: _blank_

Run ID: _blank_

## Exact proposal presented for separate owner decision

- Proposal ID: `{proposal['proposal_id']}`
- Proposal hash: `{proposal['manifest_sha256']}`
- Expiry: `{proposal['expires_on']}`
- Geometry: 48 episodes × 3 actors × C1 primary plus matched probe = **288 logical calls**
- Dispatch boundary: no C0/C2 dispatch; no capability twins; fallback disabled
- Retry exposure: at most 2 attempts per logical call, rate-limit only
- Missingness: unknown delivery is terminal missingness
- Forecast: **${proposal['budget']['forecast_usd']:.7f}**, below the **$3.00** forecast gate
- Hard not-to-exceed ceiling: **$5.00**
- Evidence hash: `{consistency['evidence_registry_sha256']}`
- Registered adapter controls: temperature `0`; maximum output `700`

### Roster

Prices are standard synchronous text input/output USD per million tokens.

| Alias | Provider | Exact model | Exact first-party route | Input / output price | Token caps |
|---|---|---|---|---:|---:|
{roster}

### Frozen contract hashes

- Runner hash: `{hashes['compiler_sha256']}`
- Adapter hash: `{hashes['adapter_sha256']}`
- Proposal schema hash: `{hashes['proposal_schema_sha256']}`
- Artifact schema hash: `{hashes['artifact_schema_sha256']}`
- Bank-set hash: `{hashes['bank_set_sha256']}`
- Request-registry-set hash: `{hashes['request_registry_set_sha256']}`
- Surface-registry-set hash: `{hashes['surface_registry_set_sha256']}`
- Analysis-contract hash: `{hashes['analysis_contract_sha256']}`
- Adjudication-contract hash: `{hashes['adjudication_contract_sha256']}`

### Unresolved pre-call facts

Unresolved facts are account entitlement, live model availability, account
rate limits, taxes, billing rounding, and regional availability or pricing.
They cannot be verified without entering a credential or provider surface.
They remain explicitly unresolved. Any material change requires a refreshed
proposal and owner review.

### Human-readable consistency statement

The proposal hash, evidence hash, geometry, budget, checkpoint, frozen contract
hashes, and blank owner fields above describe the same `PROPOSAL_ONLY` object.
The machine-readable companion is `pf002-preflight-consistency.json`, whose
checkpoint hash is `{consistency['checkpoint_sha256']}`.

## Owner gate

Approval, if granted, must be a separate hash-bound authorization record for
this exact proposal. Any roster, route, price, geometry, expiry, or budget
change requires a new proposal and a new owner decision. This request cannot
authorize itself.

No credential, provider, model, or billing surface was accessed. Calls: **0**.
Spend: **$0.00**. The pilot remains stopped.
"""


def _checkpoint_markdown(
    proposal: dict[str, Any],
    evidence: dict[str, Any],
    checkpoint: dict[str, Any],
) -> str:
    rows = "\n".join(
        "| {actor_alias} | {provider} | `{model_id}` | ${route_worst_case_usd:.7f} |".format(
            **model
        )
        for model in checkpoint["models"]
    )
    return f"""# BibleBench PF-002 Cost Checkpoint

Status: `PROPOSAL_ONLY` — **NOT AUTHORIZED**

Verified from official public documentation on {evidence['verified_on']}.
No credential or provider/model endpoint was accessed. Calls: **0**. Spend:
**$0.00**.

## Registered geometry

- 48 executable episodes
- 3 exact general-purpose actors
- C1 primary and matched observable probe
- **288 logical calls**: 144 primary and 144 probe
- Maximum 2 attempts per logical call; rate-limit retry only
- Input cap: 4,096 tokens; output cap: 700 tokens

## Exact worst-case forecast

| Alias | Provider | Model | Two-attempt worst case |
|---|---|---|---:|
{rows}

- Calculated worst case: **${checkpoint['calculated_worst_case_usd']:.7f}**
- Forecast gate: **$3.00**
- Hard not-to-exceed ceiling: **$5.00**
- Proposal hash: `{proposal['manifest_sha256']}`
- Proposal expiry: `{proposal['expires_on']}`

The forecast charges every logical call at both registered attempts and at both
token caps. Any change to this proposal requires recomputation and separate
owner approval. This checkpoint grants no authority to access credentials,
construct transport, or make calls.
"""


def build_preflight_bundle(package_root: Path) -> dict[str, bytes]:
    proposal = load_proposal(package_root / PROPOSAL_FIXTURE)
    total = validate_proposal_contract(
        proposal,
        bank_root=package_root,
        today=date.fromisoformat("2026-07-13"),
    )
    evidence = _read_json(package_root / EVIDENCE_PATH)
    _validate_evidence(proposal, evidence)
    checkpoint = _checkpoint_payload(proposal, evidence, total)
    consistency = _consistency_payload(proposal, evidence, checkpoint)
    authorization_request = _authorization_markdown(
        proposal, evidence, consistency
    ).encode("utf-8")
    consistency["authorization_request_sha256"] = _sha256(
        authorization_request
    )
    return {
        "pf002-three-model-proposal.json": _pretty_json(proposal),
        "pf002-preflight-consistency.json": _pretty_json(consistency),
        "PF002-OWNER-AUTHORIZATION-REQUEST.md": authorization_request,
        "pilot-cost-estimate.json": _pretty_json(checkpoint),
        "PILOT-COST-CHECKPOINT.md": _checkpoint_markdown(
            proposal, evidence, checkpoint
        ).encode("utf-8"),
    }


def write_preflight_bundle(package_root: Path) -> tuple[Path, ...]:
    bundle = build_preflight_bundle(package_root)
    mapping = {
        "pf002-three-model-proposal.json": package_root
        / "preflight/pf002-three-model-proposal.json",
        "pf002-preflight-consistency.json": package_root
        / "preflight/pf002-preflight-consistency.json",
        "PF002-OWNER-AUTHORIZATION-REQUEST.md": package_root
        / "preflight/PF002-OWNER-AUTHORIZATION-REQUEST.md",
        "pilot-cost-estimate.json": package_root / "pilot-cost-estimate.json",
        "PILOT-COST-CHECKPOINT.md": package_root / "PILOT-COST-CHECKPOINT.md",
    }
    written: list[Path] = []
    for name, payload in bundle.items():
        target = mapping[name]
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(payload)
        written.append(target)
    return tuple(written)
