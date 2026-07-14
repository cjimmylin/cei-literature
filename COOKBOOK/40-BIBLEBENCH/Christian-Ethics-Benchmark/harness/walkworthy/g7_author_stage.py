"""First-attempt-only orchestrator for the frozen PUBLIC G7 author stage."""
from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
from typing import Tuple

from .g7_author_contract import (
    AUTHOR_MODEL,
    AUTHOR_SYSTEM_PROMPT,
    AUTHOR_SYSTEM_PROMPT_SHA256,
    AUTHOR_USER_PROMPT_TEMPLATE,
    AUTHOR_USER_PROMPT_TEMPLATE_SHA256,
    MEMO_SHA256,
    AuthorCustodyLedger,
    build_author_request,
    validate_author_output,
)
from .g7_perturbation import (
    build_public_manifest,
    load_production_role_manifest,
    select_public_sample,
)
from .g7_runner import (
    HARD_NTE_USD,
    PRODUCTION_MANIFEST_SHA256,
    ROLE_MANIFEST_SHA256,
    ROLE_SPECS,
    AttemptLedger,
    ContractStop,
    conservative_input_bytes,
    default_transport_request_bytes,
    spec_for,
    write_once_json,
)
from .loader import load_public_split
from .openrouter_backend import OPENROUTER_URL


AUTHOR_MEMO_PATH = "00-PORTFOLIO/20260713s-opus-g7-paraphrase-author-contract.md"
AUTHOR_TIMEOUT_SECONDS = 120.0


@dataclass(frozen=True)
class AuthorStageSurface:
    items: Tuple[object, ...]
    role_manifests: Tuple[object, ...]
    manifest_sha256: str
    role_manifest_sha256: str


def _identity(value, name):
    return value.get(name) if isinstance(value, dict) else getattr(value, name)


def _sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _verify_contract_hashes(benchmark_root=None) -> None:
    if _sha256_text(AUTHOR_SYSTEM_PROMPT) != AUTHOR_SYSTEM_PROMPT_SHA256:
        raise ContractStop("G7 author system-prompt SHA-256 mismatch")
    if _sha256_text(AUTHOR_USER_PROMPT_TEMPLATE) != AUTHOR_USER_PROMPT_TEMPLATE_SHA256:
        raise ContractStop("G7 author user-prompt SHA-256 mismatch")
    if benchmark_root is not None:
        memo = Path(benchmark_root) / AUTHOR_MEMO_PATH
        if hashlib.sha256(memo.read_bytes()).hexdigest() != MEMO_SHA256:
            raise ContractStop("G7 author contract memo SHA-256 mismatch")


def build_production_author_surface(benchmark_root) -> AuthorStageSurface:
    """Load and fully verify the frozen 73-item PUBLIC author surface."""
    root = Path(benchmark_root)
    _verify_contract_hashes(root)
    population = tuple(load_public_split(
        str(root), include_exemplars=True, runnable_only=True
    ))
    sut_slugs = tuple(spec.slug for spec in ROLE_SPECS if spec.role == "sut")
    if len(sut_slugs) != 6 or len(set(sut_slugs)) != 6:
        raise ContractStop("G7 production SUT roster is not the exact six slugs")
    manifest = build_public_manifest(population, sut_slugs)
    if manifest.sha256 != PRODUCTION_MANIFEST_SHA256:
        raise ContractStop("G7 production manifest SHA-256 mismatch")
    role_manifests = tuple(sorted(
        load_production_role_manifest(population),
        key=lambda row: (row.design, row.item_id),
    ))
    items = tuple(sorted(
        select_public_sample(population), key=lambda item: (item.design, item.id)
    ))
    identities = tuple((item.design, item.id) for item in items)
    role_identities = tuple((row.design, row.item_id) for row in role_manifests)
    if len(items) != 73 or identities != role_identities:
        raise ContractStop("G7 production author surface is not exact canonical 73")
    return AuthorStageSurface(
        items, role_manifests, manifest.sha256, ROLE_MANIFEST_SHA256
    )


def _prepare_surface(surface: AuthorStageSurface):
    _verify_contract_hashes()
    if (surface.manifest_sha256 != PRODUCTION_MANIFEST_SHA256
            or surface.role_manifest_sha256 != ROLE_MANIFEST_SHA256):
        raise ContractStop("G7 author surface hash mismatch")
    items = tuple(surface.items)
    roles = tuple(surface.role_manifests)
    if not items or len(items) != len(roles):
        raise ContractStop("G7 author item/role surface mismatch")
    if items != tuple(sorted(items, key=lambda item: (item.design, item.id))):
        raise ContractStop("G7 author items are not canonical")
    if roles != tuple(sorted(
            roles, key=lambda row: (_identity(row, "design"),
                                    _identity(row, "item_id")))):
        raise ContractStop("G7 author role manifests are not canonical")
    if tuple((item.design, item.id) for item in items) != tuple(
            (_identity(row, "design"), _identity(row, "item_id")) for row in roles):
        raise ContractStop("G7 author item/role identities differ")
    keys = tuple(item.id for item in items)
    if len(set(keys)) != len(keys):
        raise ContractStop("G7 author logical item keys are not unique")
    requests = tuple(build_author_request(item, role) for item, role in zip(items, roles))
    spec = spec_for("paraphrase_author", AUTHOR_MODEL)
    if any(conservative_input_bytes(request.payload) > spec.input_envelope
           for request in requests):
        raise ContractStop("G7 author request exceeds conservative input envelope")
    return items, keys, requests, spec


def _registration(surface, keys, max_author_envelope):
    return {
        "schema_version": "walkworthy-g7-author-stage-v1",
        "surface": "production_public",
        "manifest_sha256": surface.manifest_sha256,
        "role_manifest_sha256": surface.role_manifest_sha256,
        "contract_memo_sha256": MEMO_SHA256,
        "author_system_prompt_sha256": AUTHOR_SYSTEM_PROMPT_SHA256,
        "author_user_prompt_template_sha256": AUTHOR_USER_PROMPT_TEMPLATE_SHA256,
        "author_model": AUTHOR_MODEL,
        "logical_keys": list(keys),
        "planned": len(keys),
        "planned_cap": len(keys),
        "replay_cap": len(keys),
        "post_cap": 2 * len(keys),
        "max_concurrency": 2,
        "hard_nte_usd": str(HARD_NTE_USD),
        "max_author_envelope_usd": str(max_author_envelope),
    }


def _response_body(response) -> str:
    try:
        body = response["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as exc:
        raise ContractStop("G7 author validated transport lacks exact raw body") from exc
    if not isinstance(body, str):
        raise ContractStop("G7 author validated transport body is not a string")
    return body


def _custody_state(path: Path):
    rows = ([json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]
            if path.exists() else [])
    return {
        "transport": {row["attempt_id"]: row for row in rows
                      if row.get("event") == "author_transport_custodied"},
        "outcomes": {row["attempt_id"]: row for row in rows
                     if row.get("event") == "author_transport_outcome"},
        "packets": {row["attempt_id"]: row for row in rows
                    if row.get("event") == "review_packets_custodied"},
    }


def _custody_packet_rows(path: Path):
    return _custody_state(path)["packets"]


def _attempts_by_key(ledger: AttemptLedger):
    snapshot = ledger.snapshot()
    by_key = {}
    for attempt in range(1, snapshot["posts"] + 1):
        value = ledger.attempt_snapshot(attempt)
        by_key[value["start"]["logical_key"]] = (attempt, value)
    return by_key


def _all_attempts(ledger: AttemptLedger):
    return tuple(
        (attempt, ledger.attempt_snapshot(attempt))
        for attempt in range(1, ledger.snapshot()["posts"] + 1)
    )


def _reconcile_started_attempts(
    spend, custody, custody_path, items, requests,
):
    """Close only provable custodied gaps before permitting a new POST."""
    by_key = {
        item.id: (item, request) for item, request in zip(items, requests)
    }
    attempts = _all_attempts(spend)
    state = _custody_state(custody_path)
    attempt_ids = {attempt for attempt, _snapshot in attempts}
    if set(state["transport"]) - attempt_ids:
        raise ContractStop("G7 author custody has no matching started attempt")

    for attempt, snapshot in attempts:
        start = snapshot["start"]
        item, request = by_key[start["logical_key"]]
        exact_request = default_transport_request_bytes(request.payload)
        exact_digest = hashlib.sha256(exact_request).hexdigest()
        if start["payload_sha256"] != exact_digest:
            raise ContractStop("G7 author started payload differs from rebuilt request")
        transport_row = state["transport"].get(attempt)
        if transport_row is None:
            raise ContractStop("G7 author started attempt lacks body custody")
        if (transport_row["logical_key"] != item.id
                or transport_row["payload_sha256"] != exact_digest
                or transport_row["request_json"] != exact_request.decode("utf-8")):
            raise ContractStop("G7 author custodied request binding conflict")

        custody.finish_transport(
            spend, item.id, attempt, request.payload,
            transport_row["status"], transport_row["response"],
        )
        snapshot = spend.attempt_snapshot(attempt)
        state = _custody_state(custody_path)

        finish = snapshot["finish"]
        validation = snapshot["validation"]
        if (finish is not None and finish["failure"] is None
                and validation is not None
                and validation["event"] == "validation_pending"
                and attempt not in state["packets"]):
            result = validate_author_output(
                item, request.prepared, _response_body(transport_row["response"]),
                review_submission=None, review_complete=False,
            )
            custody.record_validation(item.id, attempt, result, spend)
            state = _custody_state(custody_path)

    # Force a fresh cross-file validation before dispatching any never-started key.
    AuthorCustodyLedger(custody_path)


def _headers(api_key: str) -> dict:
    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/cjimmylin/cei-literature",
        "X-Title": "WALKWORTHY-benchmark",
    }


def run_author_surface_first_attempts(
    surface: AuthorStageSurface, out_dir, api_key, transport, max_workers=2,
):
    """Execute only missing first author attempts for an already-verified surface."""
    if type(max_workers) is not int or max_workers not in (1, 2):
        raise ContractStop("G7 author max_workers must be 1 or 2")
    if not callable(transport):
        raise ContractStop("G7 author transport must be callable")
    if not isinstance(api_key, str) or not api_key:
        raise ContractStop("G7 author API key must be supplied explicitly")
    items, keys, requests, spec = _prepare_surface(surface)
    max_author_envelope = spec.max_missing_cost * len(keys)
    registration = _registration(surface, keys, max_author_envelope)

    out = Path(out_dir)
    registration_path = out / "author-registration.json"
    if out.exists():
        if not out.is_dir() or not registration_path.exists():
            raise ContractStop("G7 author run directory lacks immutable registration")
    else:
        out.mkdir(parents=True)
    write_once_json(registration_path, registration)

    spend_path = out / "author-attempts.jsonl"
    custody_path = out / "author-custody.jsonl"
    spend = AttemptLedger(
        spend_path, expected_keys=keys, hard_nte_usd=HARD_NTE_USD,
        planned_cap=len(keys), replay_cap=len(keys), post_cap=2 * len(keys),
        max_concurrency=2,
    )
    custody = AuthorCustodyLedger(custody_path)
    _reconcile_started_attempts(
        spend, custody, custody_path, items, requests
    )
    by_key = _attempts_by_key(spend)
    missing = [(item, request) for item, request in zip(items, requests)
               if item.id not in by_key]
    inflight = sum(value[1]["finish"] is None for value in by_key.values())
    available_workers = min(max_workers, 2 - inflight)
    if missing and available_workers < 1:
        raise ContractStop("G7 author first-attempt resume has no concurrency slot")

    headers = _headers(api_key)

    def finish_one(item, request, attempt):
        try:
            status, response = transport(
                OPENROUTER_URL, headers, request.payload,
                timeout=AUTHOR_TIMEOUT_SECONDS,
            )
        except Exception as exc:  # the failed POST still consumes its first attempt
            status = None
            response = {
                "transport_exception": {
                    "type": type(exc).__name__, "message": "transport raised",
                }
            }
        outcome = custody.finish_transport(
            spend, item.id, attempt, request.payload, status, response
        )
        if outcome == "validation_pending":
            result = validate_author_output(
                item, request.prepared, _response_body(response),
                review_submission=None, review_complete=False,
            )
            custody.record_validation(item.id, attempt, result, spend)

    with ThreadPoolExecutor(max_workers=max(1, available_workers)) as executor:
        for offset in range(0, len(missing), max(1, available_workers)):
            batch = missing[offset:offset + max(1, available_workers)]
            started = [
                (item, request, spend.begin(item.id, spec, request.payload))
                for item, request in batch
            ]
            futures = [executor.submit(finish_one, *entry) for entry in started]
            for future in futures:
                future.result()

    # Reload both ledgers before deriving the immutable author checkpoint.
    custody = AuthorCustodyLedger(custody_path)
    by_key = _attempts_by_key(spend)
    packet_rows = _custody_packet_rows(custody_path)
    pending = []
    replay = []
    complete = []
    unresolved_other = []
    packet_items = []
    for item_id in keys:
        entry = by_key.get(item_id)
        if entry is None:
            unresolved_other.append(item_id)
            continue
        attempt, snapshot = entry
        finish = snapshot["finish"]
        validation = snapshot["validation"]
        if finish is None:
            unresolved_other.append(item_id)
        elif finish["failure"] is not None:
            replay.append(item_id)
        elif validation and validation["event"] == "validation_failed":
            replay.append(item_id)
        elif validation and validation["event"] == "logical_complete":
            complete.append(item_id)
        elif validation and validation["event"] == "validation_pending":
            packet = packet_rows.get(attempt)
            if packet is None:
                unresolved_other.append(item_id)
            else:
                pending.append(item_id)
                packet_items.append({
                    "item_id": item_id, "attempt_id": attempt,
                    "review_packets": packet["review_packets"],
                })
        else:
            unresolved_other.append(item_id)

    packet_export = {
        "schema_version": "walkworthy-g7-jimmy-semantic-review-v1",
        "surface": "production_public",
        "manifest_sha256": surface.manifest_sha256,
        "role_manifest_sha256": surface.role_manifest_sha256,
        "contract_memo_sha256": MEMO_SHA256,
        "items": sorted(packet_items, key=lambda row: (row["item_id"], row["attempt_id"])),
    }
    write_once_json(out / "jimmy-semantic-review-packets.json", packet_export)

    accounting = spend.snapshot()
    unresolved = sorted(set(replay + unresolved_other))
    if pending:
        status = "validation_pending_jimmy"
    elif replay:
        status = "replay_required"
    elif unresolved_other:
        status = "mechanically_unresolved"
    elif complete:
        status = "jimmy_review_applied"
    else:
        status = "no_author_attempts"
    remaining = (HARD_NTE_USD - accounting["actual"]
                 - accounting["reserved"] - accounting["inflight"])
    checkpoint = {
        "schema_version": "walkworthy-g7-author-checkpoint-v1",
        "surface": "production_public",
        "manifest_sha256": surface.manifest_sha256,
        "role_manifest_sha256": surface.role_manifest_sha256,
        "contract_memo_sha256": MEMO_SHA256,
        "author_system_prompt_sha256": AUTHOR_SYSTEM_PROMPT_SHA256,
        "author_user_prompt_template_sha256": AUTHOR_USER_PROMPT_TEMPLATE_SHA256,
        "planned": len(keys),
        "attempts": accounting["planned"],
        "posts": accounting["posts"],
        "validation_pending": len(pending),
        "replay_required": len(replay),
        "unresolved": len(unresolved),
        "actual_usd": str(accounting["actual"]),
        "reserved_usd": str(accounting["reserved"]),
        "max_author_envelope_usd": str(max_author_envelope),
        "remaining_global_nte_usd": str(remaining),
        "pending_item_ids": pending,
        "replay_item_ids": replay,
        "unresolved_item_ids": unresolved,
        "complete": False,
        "status": status,
    }
    return write_once_json(out / "author-checkpoint.json", checkpoint)


def run_author_first_attempts(
    benchmark_root, out_dir, api_key, transport, max_workers=2,
):
    """Run the exact frozen 73 PUBLIC author first attempts, never replays."""
    surface = build_production_author_surface(benchmark_root)
    return run_author_surface_first_attempts(
        surface, out_dir, api_key, transport, max_workers=max_workers
    )
