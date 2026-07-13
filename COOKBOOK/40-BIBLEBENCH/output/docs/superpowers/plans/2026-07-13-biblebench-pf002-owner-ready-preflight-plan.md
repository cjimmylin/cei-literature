# BibleBench PF-002 Owner-Ready Preflight Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a deterministic, zero-spend, owner-ready three-model PF-002 preflight packet that replaces the stale four-model checkpoint while remaining explicitly unauthorized.

**Architecture:** A small offline builder reads the already schema-validated real-roster proposal fixture plus a locally recorded official-source evidence registry. It validates the proposal through the existing fail-closed runner, then emits four mutually consistent artifacts: canonical proposal JSON, corrected cost checkpoint JSON/Markdown, owner authorization request, and consistency report. The build contains no transport and never reads credentials, adjudication data, or provider state.

**Tech Stack:** Python 3.14, standard library, existing `jsonschema`/PyYAML dependencies, pytest, JSON, Markdown.

---

### Task 1: Lock the three-model preflight contract with failing tests

**Files:**
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/tests/test_pf002_preflight.py`
- Modify: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/tests/test_cost_checkpoint.py`

- [ ] **Step 1: Add an artifact-inventory test**

Create `test_pf002_preflight.py` with these constants and first test:

```python
from __future__ import annotations

from decimal import Decimal
import json
from pathlib import Path

import pytest


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
```

- [ ] **Step 2: Add exact geometry and authority-state tests**

Append:

```python
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
```

- [ ] **Step 3: Replace the stale four-model cost test with independent recomputation**

Replace `test_cost_checkpoint_is_exact_recomputable_and_non_authorizing` with:

```python
def test_cost_checkpoint_is_exact_recomputable_and_non_authorizing() -> None:
    data = json.loads(CHECKPOINT.read_text(encoding="utf-8"))
    assert data["estimate_version"] == "pf002-three-model-preflight-v1"
    assert data["status"] == "PROPOSAL_ONLY"
    assert data["authorized"] is False
    assert data["calls_made"] == 0
    assert Decimal(str(data["spend_usd"])) == Decimal("0")
    assert data["geometry"] == {
        "actors": 3,
        "episodes": 48,
        "primary_calls": 144,
        "probe_calls": 144,
        "logical_calls": 288,
        "maximum_attempts_per_logical_call": 2,
    }
    total = Decimal("0")
    for actor in data["models"]:
        expected = Decimal(192) * (
            Decimal(4096) * Decimal(str(actor["input_usd_per_million_tokens"]))
            + Decimal(700) * Decimal(str(actor["output_usd_per_million_tokens"]))
        ) / Decimal("1000000")
        assert Decimal(str(actor["route_worst_case_usd"])) == expected
        total += expected
    assert Decimal(str(data["calculated_worst_case_usd"])) == total
    assert Decimal(str(data["forecast_usd"])) == total
    assert total <= Decimal("3")
    assert Decimal(str(data["forecast_limit_usd"])) == Decimal("3")
    assert Decimal(str(data["hard_nte_usd"])) == Decimal("5")
```

- [ ] **Step 4: Run the new contract tests and observe RED**

Run:

```bash
cd COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT
/opt/homebrew/bin/python3 -m pytest tests/test_pf002_preflight.py tests/test_cost_checkpoint.py -q
```

Expected: FAIL because the preflight directory does not exist and the active cost estimate still describes four models and 1,356 maximum calls.

- [ ] **Step 5: Commit the RED contract**

```bash
git add COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/tests/test_pf002_preflight.py \
  COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/tests/test_cost_checkpoint.py
git commit -m "BibleBench: lock PF-002 preflight contract"
```

### Task 2: Record official public model and price evidence

**Files:**
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/preflight/verified-model-evidence.json`
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/preflight/OFFICIAL-SOURCE-VERIFICATION.md`
- Modify: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/tests/test_pf002_preflight.py`

- [ ] **Step 1: Verify only first-party public sources**

Open and verify these official pages without credentials or provider API calls:

```text
https://developers.openai.com/api/docs/models/gpt-5-nano
https://platform.openai.com/docs/guides/text-generation
https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite
https://ai.google.dev/gemini-api/docs/pricing
https://ai.google.dev/api/generate-content
https://platform.claude.com/docs/en/about-claude/models/overview
https://docs.anthropic.com/en/api/messages
```

Record exact identifiers, standard synchronous input/output prices per million
tokens, context window, maximum output, route family, source URL, page title,
and verification date. If any exact fact is not supported, stop and mark the
packet incomplete rather than substituting an aggregator.

- [ ] **Step 2: Create the closed evidence registry**

Write `verified-model-evidence.json` with this shape and the source-verified
values:

```json
{
  "registry_version": "pf002-official-model-evidence-v1",
  "classification": "PUBLIC_DOCUMENTATION_ONLY",
  "verified_on": "2026-07-13",
  "credentials_accessed": false,
  "provider_calls_made": 0,
  "spend_usd": 0,
  "actors": [
    {
      "actor_alias": "actor-alpha",
      "provider": "OpenAI",
      "model_id": "gpt-5-nano-2025-08-07",
      "route_id": "openai/first-party/responses",
      "api_family": "responses",
      "input_usd_per_million_tokens": 0.05,
      "output_usd_per_million_tokens": 0.4,
      "context_window_tokens": 400000,
      "maximum_output_tokens": 128000,
      "official_sources": [
        "https://developers.openai.com/api/docs/models/gpt-5-nano",
        "https://platform.openai.com/docs/guides/text-generation"
      ]
    },
    {
      "actor_alias": "actor-beta",
      "provider": "Google",
      "model_id": "gemini-2.5-flash-lite",
      "route_id": "google/first-party/generate-content",
      "api_family": "generate_content",
      "input_usd_per_million_tokens": 0.1,
      "output_usd_per_million_tokens": 0.4,
      "context_window_tokens": 1048576,
      "maximum_output_tokens": 65536,
      "official_sources": [
        "https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite",
        "https://ai.google.dev/gemini-api/docs/pricing",
        "https://ai.google.dev/api/generate-content"
      ]
    },
    {
      "actor_alias": "actor-gamma",
      "provider": "Anthropic",
      "model_id": "claude-haiku-4-5-20251001",
      "route_id": "anthropic/first-party/messages",
      "api_family": "messages",
      "input_usd_per_million_tokens": 1,
      "output_usd_per_million_tokens": 5,
      "context_window_tokens": 200000,
      "maximum_output_tokens": 64000,
      "official_sources": [
        "https://platform.claude.com/docs/en/about-claude/models/overview",
        "https://docs.anthropic.com/en/api/messages"
      ]
    }
  ]
}
```

- [ ] **Step 3: Add official-source and proposal-consistency tests**

Append to `test_pf002_preflight.py`:

```python
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
    from urllib.parse import urlparse
    for actor in proposal["actors"]:
        row = evidence_by_alias[actor["actor_alias"]]
        assert row["provider"] == actor["provider"]
        assert row["model_id"] == actor["model_id"]
        assert row["route_id"] == actor["route"]["route_id"]
        assert row["input_usd_per_million_tokens"] == actor["price"]["input_usd"]
        assert row["output_usd_per_million_tokens"] == actor["price"]["output_usd"]
        assert {urlparse(url).hostname for url in row["official_sources"]} <= allowed_hosts
```

- [ ] **Step 4: Run the evidence tests**

Run:

```bash
/opt/homebrew/bin/python3 -m pytest tests/test_pf002_preflight.py::test_evidence_registry_is_public_first_party_and_matches_proposal -q
```

Expected: FAIL until the canonical proposal is emitted in Task 3; the evidence
file itself must parse and contain exactly three actors.

- [ ] **Step 5: Commit the evidence record**

```bash
git add COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/preflight/verified-model-evidence.json \
  COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/preflight/OFFICIAL-SOURCE-VERIFICATION.md \
  COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/tests/test_pf002_preflight.py
git commit -m "BibleBench: record PF-002 official model evidence"
```

### Task 3: Implement the deterministic offline preflight builder

**Files:**
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/src/biblebench_pilot/preflight.py`
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/tools/build_pf002_preflight.py`
- Modify: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/tests/test_pf002_preflight.py`

- [ ] **Step 1: Add deterministic-build and no-network tests**

Append:

```python
def test_preflight_builder_is_deterministic_and_offline(tmp_path: Path, monkeypatch) -> None:
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
```

- [ ] **Step 2: Run and observe RED**

Run:

```bash
/opt/homebrew/bin/python3 -m pytest tests/test_pf002_preflight.py::test_preflight_builder_is_deterministic_and_offline tests/test_pf002_preflight.py::test_preflight_builder_imports_no_transport_or_credentials -q
```

Expected: FAIL because `biblebench_pilot.preflight` does not exist.

- [ ] **Step 3: Implement the builder boundary**

Create `preflight.py` with these public functions and constants:

```python
from __future__ import annotations

from copy import deepcopy
from datetime import date
from decimal import Decimal
import hashlib
import json
from pathlib import Path
from typing import Any

from .contracts import canonical_json_bytes, canonical_sha256
from .mvp_runner import load_proposal, validate_proposal_contract


GENERATOR_VERSION = "pf002-owner-ready-preflight-v1"
PROPOSAL_FIXTURE = Path("tests/fixtures/mvp-proposal-real-unauthorized.json")
EVIDENCE_PATH = Path("preflight/verified-model-evidence.json")


def _pretty_json(value: dict[str, Any]) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True) + "\n").encode("utf-8")


def _read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if type(value) is not dict:
        raise ValueError(f"expected object: {path}")
    return value


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def build_preflight_bundle(package_root: Path) -> dict[str, bytes]:
    proposal = load_proposal(package_root / PROPOSAL_FIXTURE)
    total = validate_proposal_contract(
        proposal, bank_root=package_root, today=date.fromisoformat("2026-07-13")
    )
    evidence = _read_json(package_root / EVIDENCE_PATH)
    _validate_evidence(proposal, evidence)
    proposal_bytes = _pretty_json(proposal)
    checkpoint = _checkpoint_payload(proposal, evidence, total)
    consistency = _consistency_payload(proposal, evidence, checkpoint)
    return {
        "pf002-three-model-proposal.json": proposal_bytes,
        "pf002-preflight-consistency.json": _pretty_json(consistency),
        "PF002-OWNER-AUTHORIZATION-REQUEST.md": _authorization_markdown(
            proposal, evidence, consistency
        ).encode("utf-8"),
        "pilot-cost-estimate.json": _pretty_json(checkpoint),
        "PILOT-COST-CHECKPOINT.md": _checkpoint_markdown(
            proposal, evidence, checkpoint
        ).encode("utf-8"),
    }
```

Implement `_validate_evidence`, `_checkpoint_payload`, `_consistency_payload`,
`_authorization_markdown`, and `_checkpoint_markdown` as pure functions. They
must require exact actor-by-alias equality for provider, model, route, price,
context, and output limits; render the exact 288-call geometry; retain
`PROPOSAL_ONLY`/`authorized: false`; display the independently validated total;
and include zero calls/spend plus the blank owner fields.

- [ ] **Step 4: Add a write command with exclusive target mapping**

Append:

```python
def write_preflight_bundle(package_root: Path) -> tuple[Path, ...]:
    bundle = build_preflight_bundle(package_root)
    mapping = {
        "pf002-three-model-proposal.json": package_root / "preflight/pf002-three-model-proposal.json",
        "pf002-preflight-consistency.json": package_root / "preflight/pf002-preflight-consistency.json",
        "PF002-OWNER-AUTHORIZATION-REQUEST.md": package_root / "preflight/PF002-OWNER-AUTHORIZATION-REQUEST.md",
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
```

Create `tools/build_pf002_preflight.py`:

```python
from __future__ import annotations

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from biblebench_pilot.preflight import write_preflight_bundle  # noqa: E402


if __name__ == "__main__":
    for path in write_preflight_bundle(ROOT):
        print(path)
```

- [ ] **Step 5: Run the builder tests**

Run:

```bash
/opt/homebrew/bin/python3 -m pytest tests/test_pf002_preflight.py -q
```

Expected: remaining artifact-existence tests FAIL until Task 4 runs the builder;
pure-function, deterministic, offline, and authority-state tests PASS.

- [ ] **Step 6: Commit the builder**

```bash
git add COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/src/biblebench_pilot/preflight.py \
  COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/tools/build_pf002_preflight.py \
  COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/tests/test_pf002_preflight.py
git commit -m "BibleBench: build deterministic PF-002 preflight"
```

### Task 4: Generate and validate the owner-facing packet

**Files:**
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/preflight/pf002-three-model-proposal.json`
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/preflight/pf002-preflight-consistency.json`
- Create: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/preflight/PF002-OWNER-AUTHORIZATION-REQUEST.md`
- Modify: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/pilot-cost-estimate.json`
- Modify: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/PILOT-COST-CHECKPOINT.md`
- Modify: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/tests/test_pf002_preflight.py`

- [ ] **Step 1: Run the offline builder**

```bash
cd COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT
/opt/homebrew/bin/python3 tools/build_pf002_preflight.py
```

Expected: exactly five printed output paths and no network, credential, or
provider activity.

- [ ] **Step 2: Add cross-artifact hash and rendering tests**

Append:

```python
def test_consistency_record_binds_every_owner_facing_artifact() -> None:
    consistency = json.loads(CONSISTENCY.read_text(encoding="utf-8"))
    proposal = json.loads(PROPOSAL.read_text(encoding="utf-8"))
    checkpoint = json.loads(CHECKPOINT_JSON.read_text(encoding="utf-8"))
    assert consistency["classification"] == "PROPOSAL_ONLY"
    assert consistency["authorized"] is False
    assert consistency["proposal_manifest_sha256"] == proposal["manifest_sha256"]
    assert consistency["geometry"] == proposal["geometry"]
    assert consistency["budget"] == proposal["budget"]
    assert consistency["checkpoint_sha256"] == __import__("hashlib").sha256(
        (json.dumps(checkpoint, indent=2, sort_keys=True) + "\n").encode("utf-8")
    ).hexdigest()


def test_authorization_request_has_blank_owner_fields_and_exact_stop_gate() -> None:
    text = AUTH_REQUEST.read_text(encoding="utf-8")
    assert "Status: `NOT_AUTHORIZED`" in text
    assert "Owner: _blank_" in text
    assert "Approval reference: _blank_" in text
    assert "Authorization nonce: _blank_" in text
    assert "Run ID: _blank_" in text
    assert "No credential, provider, model, or billing surface was accessed" in text
    assert "288" in text and "$3.00" in text and "$5.00" in text
```

- [ ] **Step 3: Run focused tests**

```bash
/opt/homebrew/bin/python3 -m pytest tests/test_pf002_preflight.py tests/test_cost_checkpoint.py tests/test_mvp_runner.py -q
```

Expected: PASS.

- [ ] **Step 4: Prove byte reproducibility**

```bash
shasum -a 256 preflight/pf002-three-model-proposal.json \
  preflight/pf002-preflight-consistency.json \
  preflight/PF002-OWNER-AUTHORIZATION-REQUEST.md \
  pilot-cost-estimate.json PILOT-COST-CHECKPOINT.md
/opt/homebrew/bin/python3 tools/build_pf002_preflight.py
shasum -a 256 preflight/pf002-three-model-proposal.json \
  preflight/pf002-preflight-consistency.json \
  preflight/PF002-OWNER-AUTHORIZATION-REQUEST.md \
  pilot-cost-estimate.json PILOT-COST-CHECKPOINT.md
```

Expected: both hash sets are identical.

- [ ] **Step 5: Commit the generated packet**

```bash
git add COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/preflight \
  COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/pilot-cost-estimate.json \
  COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/PILOT-COST-CHECKPOINT.md \
  COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/tests/test_pf002_preflight.py
git commit -m "BibleBench: generate owner-ready PF-002 packet"
```

### Task 5: Close the zero-spend preflight session

**Files:**
- Modify: `COOKBOOK/40-BIBLEBENCH/ACTIVE-CRITICAL-PATHS.md`
- Modify: `COOKBOOK/40-BIBLEBENCH/project-dashboard.html`
- Modify: `COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT/preflight/pf002-preflight-consistency.json` only if the final verification record has a registered test-count field

- [ ] **Step 1: Run integrated verification**

```bash
cd COOKBOOK/40-BIBLEBENCH/BIBLEBENCH-PILOT
/opt/homebrew/bin/python3 -m pytest tests -q
```

Expected: all tests pass except already registered environment-dependent skips;
no provider, credential, or spend activity occurs.

- [ ] **Step 2: Run fail-closed semantic checks**

```bash
/opt/homebrew/bin/python3 -m pytest \
  tests/test_pf002_preflight.py \
  tests/test_mvp_runner.py::test_real_proposal_fail_closed_classes \
  tests/test_mvp_runner.py::test_recomputed_worst_case_above_three_dollars_is_rejected \
  tests/test_mvp_runner.py::test_pretransport_authorization_fail_closed_classes -q
```

Expected: PASS.

- [ ] **Step 3: Review the packet against the design**

Check every requirement in
`output/docs/superpowers/specs/2026-07-13-biblebench-pf002-owner-ready-preflight-design.md`.
Record only P0/P1 findings as blockers. Confirm exact roster, 288-call geometry,
official public evidence, deterministic decimal cost, blank owner fields,
unauthorized state, no adjudication data, no transport, and no spend.

- [ ] **Step 4: Update living status surfaces**

Update only the consolidated BibleBench sections to state:

```text
The exact three-model PF-002 proposal packet is complete, source-verified,
forecast at or below $3, capped at $5, and NOT_AUTHORIZED. Owner pass-one gold
and separate exact-manifest approval remain the only pre-call gates. Spend is
$0.00 and no credential/provider was accessed.
```

Preserve all newer WALKWORTHY and WCF content and append one dashboard history
entry; do not rewrite prior history.

- [ ] **Step 5: Final path-scoped commit**

```bash
git diff --check -- . ':(exclude)**/*.pdf'
git log -1 --oneline
git add COOKBOOK/40-BIBLEBENCH/ACTIVE-CRITICAL-PATHS.md \
  COOKBOOK/40-BIBLEBENCH/project-dashboard.html
git commit -m "BibleBench: freeze zero-spend PF-002 preflight"
```

- [ ] **Step 6: Stop at the owner gate**

Report the exact proposal hash, roster, cost, expiry, tests, and $0 spend. Do not
create an owner record, fill authorization fields, access a credential, call a
provider, or start the pilot.
