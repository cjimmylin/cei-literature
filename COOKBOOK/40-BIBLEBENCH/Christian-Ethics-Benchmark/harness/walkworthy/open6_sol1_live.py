"""Authorized, fail-closed live driver for WALKWORTHY OPEN6-SOL1.

The data-bearing execution engines remain in :mod:`open6_sol1_run` and
:mod:`open6_sol1_judge_run`.  This module composes their registered seams, freezes
the public same-roster catalog observation, runs non-evidence OAuth canaries, and
enforces the combined Sol turn cap.  Importing this module performs no network or
credential access.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import subprocess
import threading
import urllib.error
import urllib.request
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Callable, Optional

from .clients import ModelResponse
from .open6_sol1 import (
    HARD_NTE_USD,
    SOL_HARD_TURN_CAP,
    SOL_NOMINAL_TURNS,
    SOL_RESERVE_TURNS,
    canonical_json_bytes,
)
from .open6_sol1_judge import (
    JudgeBatch,
    ScoringUnit,
    build_judge_request,
    design_score_schema,
    validate_judge_result,
)
from .open6_sol1_judge_run import (
    JUDGE_ATTEMPT_CUSTODY_NAME,
    JUDGE_PLAN_NAME,
    JUDGE_RESULT_NAME,
    JUDGE_UNRESOLVED_NAME,
    prepare_judge_plan,
    run_judging,
    status as judge_status,
)
from .open6_sol1_run import (
    AppendOnlyStore,
    CALL_CACHE_NAME,
    EXECUTION_NAME,
    TERMINAL_UNRESOLVED_NAME,
    SOL_ATTEMPT_CUSTODY_NAME,
    checkpoint,
    prepare_run,
    register_catalog_revalidation,
    register_catalog_snapshot,
    run_canary,
    run_surface,
    status as sut_status,
    validate_catalog_snapshot,
    validate_catalog_revalidations,
    value_sha256,
)
from .open6_sol1_runtime import (
    BudgetStop,
    ContractStop,
    DEEPSEEK_EXCEPTION_LOGICAL_KEY,
    DEEPSEEK_EXCEPTION_MARKER_NAME,
    DEEPSEEK_EXCEPTION_MODEL,
    OpenRouterAttemptLedger,
    OpenRouterPilotClient,
    OpenRouterRunResult,
    SOL_MODEL,
    SUT_SPECS,
    SolExecClient,
    SolResult,
    SolTaskLedger,
    ThreadStop,
)
from .openrouter_backend import _default_transport, load_openrouter_key


CATALOG_ENDPOINT_PREFIX = "https://openrouter.ai/api/v1/models/"
CATALOG_ENDPOINT_SUFFIX = "/endpoints"
CANARY_ARTIFACT_NAME = "canary-gate.json"
OFFLINE_DRY_RUN_SUMMARY_NAME = "offline-dry-run-summary.json"
CANARY_SOL_LEDGER_NAME = "canary-sol-attempts.jsonl"
CANARY_SOL_CUSTODY_NAME = "canary-sol-attempt-custody.jsonl"
CANARY_SOL_RESULT_NAME = "canary-sol-results.jsonl"
STOP_CHECKPOINT_NAME = "unattended-stops.jsonl"
OPENROUTER_LEDGER_NAME = "openrouter-attempts.jsonl"
SOL_LEDGER_NAME = "sol-attempts.jsonl"
SAFEST_EXECUTE_TEMPLATE = (
    "python -m walkworthy.open6_sol1_live execute --benchmark-root {benchmark_root} "
    "--manifest {manifest} --offline-run-dir {offline_run_dir} --run-dir {run_dir}"
)

_AUTHORIZATION_MEMOS = (
    "00-PORTFOLIO/20260714-jimmy-open6-sol1-authorization.md",
    "00-PORTFOLIO/20260714-jimmy-open6-sol1-full-execution-authorization.md",
    "00-PORTFOLIO/20260714-jimmy-open6-sol1-resume-authorization.md",
    "00-PORTFOLIO/20260714-jimmy-open6-sol1-unattended-execution-order.md",
)
DEEPSEEK_EXCEPTION_AUTHORIZATION_MEMO = (
    "00-PORTFOLIO/"
    "20260715-jimmy-open6-sol1-deepseek-exception-authorization.md")
DEEPSEEK_EXCEPTION_AUTHORIZATION_SHA256 = (
    "b5ed535ad36a69309fee52e55f4e19a09510c42cf18ef7802f5988cb0be8317f")
_SOL_QUOTA_PATTERNS = (
    "usage limit", "usage_limit", "quota exceeded", "insufficient quota",
)
EXPECTED_SOL_CANARY_HASHES = {
    "classifier": {
        "prompt": "e116ddc3460d7630244d0161f34962851fe974edb8b66360681411bbe385633c",
        "schema": "d40baa5decd83d718b9cb64bf9e61af5fa5634930cb9b569bfc75890e0221a35",
    },
    "judge": {
        "prompt": "2cb5231c24c2ea8d1b371483fca415b48130ee482ca784f3acaaafa0b85ac646",
        "schema": "617bd71a32816adfc00e600540e7c3a15157de0b82e8088b56998ed41abf8076",
    },
}


def _sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _hash(value) -> str:
    return _sha256_bytes(canonical_json_bytes(value))


def _text_hash(value: str) -> str:
    return _sha256_bytes(value.encode("utf-8"))


def _canonical_decimal(value, label) -> Decimal:
    if isinstance(value, bool) or not isinstance(
            value, (str, int, float, Decimal)):
        raise ContractStop(f"invalid catalog {label} pricing")
    try:
        result = Decimal(str(value))
    except InvalidOperation as exc:
        raise ContractStop(f"invalid catalog {label} pricing") from exc
    if not result.is_finite() or result < 0:
        raise ContractStop(f"invalid catalog {label} pricing")
    return result


def _per_million_string(per_token, registered_value, label) -> str:
    per_million = _canonical_decimal(per_token, label) * Decimal(1_000_000)
    registered = _canonical_decimal(registered_value, label)
    if per_million == registered:
        return str(registered_value)
    return format(per_million.normalize(), "f")


def _default_fetch_json(url: str) -> dict:  # pragma: no cover - live network seam
    request = urllib.request.Request(
        url, headers={"Accept": "application/json"}, method="GET")
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            if response.getcode() != 200:
                raise ContractStop(
                    f"OpenRouter catalog HTTP {response.getcode()}")
            value = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        raise ContractStop(f"OpenRouter catalog HTTP {exc.code}") from exc
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ContractStop("OpenRouter catalog fetch failed") from exc
    if not isinstance(value, dict):
        raise ContractStop("OpenRouter catalog response is not an object")
    return value


def fetch_catalog_snapshot(manifest: dict, *, fetch_json=None,
                           fetched_at: str) -> dict:
    """Fetch and normalize exact endpoint observations without a credential."""
    if (not isinstance(manifest, dict)
            or not isinstance(fetched_at, str) or not fetched_at):
        raise ContractStop("invalid catalog freeze input")
    fetch_json = fetch_json or _default_fetch_json
    registered = manifest.get("openrouter", {}).get("models")
    if (not isinstance(registered, list) or len(registered) != len(SUT_SPECS)
            or [row.get("slug") for row in registered]
            != [spec.slug for spec in SUT_SPECS]):
        raise ContractStop("catalog fetch roster differs from registration")
    urls = []
    raw_responses = []
    models = []
    for row in registered:
        slug = row["slug"]
        url = CATALOG_ENDPOINT_PREFIX + slug + CATALOG_ENDPOINT_SUFFIX
        raw = fetch_json(url)
        urls.append(url)
        raw_responses.append({"url": url, "response": copy.deepcopy(raw)})
        data = raw.get("data") if isinstance(raw, dict) else None
        if (not isinstance(data, dict) or data.get("id") != slug
                or not isinstance(data.get("endpoints"), list)
                or not data["endpoints"]):
            raise ContractStop(f"catalog model identity mismatch: {slug}")
        providers = []
        for endpoint in data["endpoints"]:
            pricing = endpoint.get("pricing") if isinstance(endpoint, dict) else None
            provider = (endpoint.get("provider_name")
                        if isinstance(endpoint, dict) else None)
            if not isinstance(provider, str) or not provider.strip():
                provider = endpoint.get("name") if isinstance(endpoint, dict) else None
            if (not isinstance(provider, str) or not provider.strip()
                    or not isinstance(pricing, dict)
                    or "prompt" not in pricing or "completion" not in pricing):
                raise ContractStop(f"invalid catalog provider pricing: {slug}")
            providers.append({
                "provider": provider.strip(),
                "input_per_m_usd": _per_million_string(
                    pricing["prompt"], row["input_per_m_usd"], "input"),
                "output_per_m_usd": _per_million_string(
                    pricing["completion"], row["output_per_m_usd"], "output"),
            })
        models.append({"slug": slug, "providers": providers})
    return {
        "fetched_at": fetched_at,
        "source_urls": urls,
        "models": models,
        "raw_api_responses": raw_responses,
    }


def freeze_catalog(benchmark_root, manifest_path, run_dir, *, fetched_at,
                   fetch_json=None):
    manifest = prepare_run(benchmark_root, manifest_path, run_dir)
    validate_live_authority(manifest)
    raw = fetch_catalog_snapshot(
        manifest, fetch_json=fetch_json, fetched_at=fetched_at)
    return register_catalog_snapshot(
        benchmark_root, manifest_path, run_dir, raw)


def revalidate_catalog(benchmark_root, manifest_path, run_dir, *, fetched_at,
                       recovery_trigger, fetch_json=None):
    manifest = prepare_run(benchmark_root, manifest_path, run_dir)
    validate_live_authority(manifest)
    raw = fetch_catalog_snapshot(
        manifest, fetch_json=fetch_json, fetched_at=fetched_at)
    return register_catalog_revalidation(
        benchmark_root, manifest_path, run_dir, raw,
        recovery_trigger=recovery_trigger)


def materialize_deepseek_exception(
        benchmark_root, manifest_path, run_dir, *, authorization_path):
    """Bind Jimmy's one-attempt exception to the two failed canary attempts."""
    root = Path(benchmark_root)
    expected_memo = root / DEEPSEEK_EXCEPTION_AUTHORIZATION_MEMO
    supplied_memo = Path(authorization_path)
    if (supplied_memo.resolve() != expected_memo.resolve()
            or not supplied_memo.is_file()
            or _sha256_bytes(supplied_memo.read_bytes())
            != DEEPSEEK_EXCEPTION_AUTHORIZATION_SHA256):
        raise ContractStop("DeepSeek exception authorization mismatch")
    manifest = prepare_run(benchmark_root, manifest_path, run_dir)
    validate_live_authority(manifest)
    revalidations = validate_catalog_revalidations(
        benchmark_root, manifest_path, run_dir)
    if not revalidations:
        raise ContractStop("DeepSeek exception requires catalog revalidation")
    latest = revalidations[-1]
    if (latest.get("recovery_trigger") != "provider_recovery"
            or not any(row.get("slug") == DEEPSEEK_EXCEPTION_MODEL
                       for row in latest.get("eligible_providers", []))):
        raise ContractStop("DeepSeek exception catalog eligibility mismatch")
    ledger = OpenRouterAttemptLedger(
        Path(run_dir) / OPENROUTER_LEDGER_NAME,
        _allow_inflight_on_open=True)
    history = list(ledger.history(DEEPSEEK_EXCEPTION_LOGICAL_KEY))
    if len(history) != 2:
        raise ContractStop("DeepSeek exception attempt history mismatch")
    snapshots = [ledger.attempt_snapshot(value) for value in history]
    starts = [row["start"] for row in snapshots]
    finishes = [row["finish"] for row in snapshots]
    if (any(row is None for row in finishes)
            or [row.get("status") for row in finishes] != [404, 404]
            or any(row.get("failure") != "http_failure" for row in finishes)
            or any(row.get("requested_model") != DEEPSEEK_EXCEPTION_MODEL
                   or row.get("logical_key") != DEEPSEEK_EXCEPTION_LOGICAL_KEY
                   for row in starts)
            or len({row.get("payload_sha256") for row in starts}) != 1
            or len({row.get("ceiling_max_usd") for row in starts}) != 1):
        raise ContractStop("DeepSeek exception prior custody mismatch")
    marker = {
        "schema_version": "walkworthy.open6-sol1.deepseek-exception.v1",
        "pilot": manifest["pilot"],
        "authorization_memo_sha256":
            DEEPSEEK_EXCEPTION_AUTHORIZATION_SHA256,
        "logical_key": DEEPSEEK_EXCEPTION_LOGICAL_KEY,
        "requested_model": DEEPSEEK_EXCEPTION_MODEL,
        "prior_attempt_ids": history,
        "prior_statuses": [404, 404],
        "payload_sha256": starts[0]["payload_sha256"],
        "ceiling_max_usd": starts[0]["ceiling_max_usd"],
        "catalog_revalidation_logical_key": latest["logical_key"],
        "catalog_revalidation_record_sha256": latest["record_sha256"],
        "maximum_additional_attempts": 1,
    }
    target = Path(run_dir) / DEEPSEEK_EXCEPTION_MARKER_NAME
    expected = canonical_json_bytes(marker)
    if target.exists():
        if target.read_bytes() != expected:
            raise ContractStop("immutable DeepSeek exception marker mismatch")
    else:
        with target.open("xb") as handle:
            handle.write(expected)
    OpenRouterAttemptLedger(
        Path(run_dir) / OPENROUTER_LEDGER_NAME,
        _allow_inflight_on_open=True)
    return marker


def validate_live_authority(manifest: dict) -> bool:
    authorization = manifest.get("authorization") if isinstance(manifest, dict) else None
    live = authorization.get("live_execution") if isinstance(authorization, dict) else None
    if (not isinstance(authorization, dict)
            or tuple(authorization.get("owner_memos", ())) != _AUTHORIZATION_MEMOS
            or not isinstance(live, dict)
            or live.get("authorized") is not True
            or live.get("credential_access_at_call_time") is not True
            or live.get("unattended") is not True
            or live.get("soft_checkpoint_usd") != "15.00"
            or live.get("projection_continue_ceiling_usd") != "23.00"
            or live.get("hard_nte_usd") != HARD_NTE_USD
            or live.get("resume_only_missing") is not True
            or live.get("permanent_missingness_continues_unaffected_work") is not True):
        raise ContractStop("OPEN6-SOL1 live authorization mismatch")
    return True


def validate_offline_gate(sut: dict, judge: dict) -> bool:
    if (not isinstance(sut, dict) or not isinstance(judge, dict)
            or sut.get("run_mode") != "offline_fake"
            or sut.get("fully_complete") is not True
            or sut.get("holdout_loaded") is not False
            or judge.get("judge_complete") is not True
            or judge.get("single_judge_only") is not True
            or judge.get("holdout_loaded") is not False):
        raise ContractStop("complete offline dry run gate not satisfied")
    return True


def validate_live_execution_config(api_key, max_workers) -> bool:
    if (not isinstance(api_key, str) or not api_key.strip()
            or type(max_workers) is not int or not 1 <= max_workers <= 2):
        raise ContractStop("invalid OPEN6-SOL1 live execution configuration")
    return True


def _first_schema_value(schema):
    if "const" in schema:
        return copy.deepcopy(schema["const"])
    if "enum" in schema:
        return copy.deepcopy(schema["enum"][0])
    kind = schema.get("type")
    if kind == "object":
        return {
            key: _first_schema_value(schema["properties"][key])
            for key in schema.get("required", [])
        }
    if kind == "array":
        count = schema.get("minItems", 0)
        item_schema = schema.get("items", {})
        keys = (item_schema.get("properties", {})
                .get("unit_key", {}).get("enum"))
        if isinstance(keys, list) and len(keys) == count:
            values = []
            for key in keys:
                value = _first_schema_value(item_schema)
                value["unit_key"] = key
                values.append(value)
            return values
        return [_first_schema_value(item_schema) for _ in range(count)]
    if kind == "string":
        return "offline-fake"
    if kind in ("integer", "number"):
        return schema.get("minimum", 0)
    if kind == "boolean":
        return False
    if kind == "null":
        return None
    raise ContractStop("offline fake encountered unsupported JSON schema")


class OfflineFakeSutClient:
    """Deterministic, credential-free delegate for the complete dry run."""

    def __init__(self, spec, items_by_id):
        self.spec = spec
        self.items_by_id = items_by_id

    def complete(self, logical_key, messages, system=None,
                 response_validator=None):
        request_material = {
            "model": self.spec.slug, "system": system,
            "messages": [{"role": message.role, "content": message.content}
                         for message in messages],
        }
        response = ModelResponse(
            text=("Offline deterministic fake response "
                  + _hash(request_material)[:24] + "."),
            model=self.spec.slug,
            family=self.spec.slug.split("/", 1)[0], usage={})
        body = {
            "model": self.spec.slug,
            "choices": [{"message": {"content": response.text}}],
            "usage": {"prompt_tokens": 0, "completion_tokens": 0, "cost": 0},
        }
        if (response_validator is not None
                and response_validator(response, body) is not True):
            parts = logical_key.split(":")
            if len(parts) < 5 or parts[-2] != "allocation":
                raise ContractStop("offline fake validator failed outside allocation")
            item = self.items_by_id.get(parts[-3])
            allocation = (item.extras.get("allocation")
                          if item is not None else None)
            if not isinstance(allocation, dict):
                raise ContractStop("offline fake allocation item missing")
            tokens = list(allocation.get("tokens") or [])
            budget = Decimal(str(allocation.get("budget", 0)))
            if tokens:
                each = budget / len(tokens)
                text = "allocation: {" + ", ".join(
                    f"{token}: {format(each, '.8f')}" for token in tokens) + "}"
            else:
                text = "allocation: {}"
            response = ModelResponse(
                text=text, model=self.spec.slug,
                family=self.spec.slug.split("/", 1)[0], usage={})
            body["choices"][0]["message"]["content"] = text
            if response_validator(response, body) is not True:
                raise ContractStop("offline fake allocation does not parse")
        payload = {
            "model": self.spec.slug,
            "messages": ([{"role": "system", "content": system}]
                         if system else []) + [
                {"role": message.role, "content": message.content}
                for message in messages
            ],
            "max_tokens": self.spec.max_tokens,
            "provider": self.spec.provider_prefs,
        }
        return OpenRouterRunResult(
            response=response, body=body, payload=payload,
            attempt_ids=(int(_text_hash(logical_key), 16),))


class OfflineFakeSolClient:
    """Schema-valid deterministic router/judge with complete fake custody."""

    def __init__(self, starting_attempt=0):
        if type(starting_attempt) is not int or starting_attempt < 0:
            raise ContractStop("invalid offline Sol attempt start")
        self.attempt_sink = None
        self._lock = threading.Lock()
        self._attempt = starting_attempt

    def run_json(self, logical_key, prompt, schema, value_validator=None):
        value = _first_schema_value(schema)
        if value_validator is not None and value_validator(value) is not True:
            raise ContractStop("offline fake Sol value failed registered semantics")
        final_text = json.dumps(
            value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        trace = '{"type":"turn.completed","usage":{}}\n'
        with self._lock:
            self._attempt += 1
            attempt_id = self._attempt
        if self.attempt_sink is not None:
            self.attempt_sink({
                "logical_key": logical_key,
                "attempt_id": attempt_id,
                "prompt": prompt,
                "schema": copy.deepcopy(schema),
                "final_text": final_text,
                "trace_jsonl": trace,
                "stderr": "",
                "returncode": 0,
                "error_class": None,
                "payload_sha256": _text_hash(prompt),
                "schema_sha256": _hash(schema),
                "trace_sha256": _text_hash(trace),
                "response_sha256": _text_hash(final_text),
                "error_sha256": None,
                "cli_version": "offline-fake",
                "usage": {},
            })
        return SolResult(
            value=value, prompt=prompt, schema=copy.deepcopy(schema),
            final_text=final_text, trace_jsonl=trace,
            cli_version="offline-fake", usage={},
            attempt_ids=(attempt_id,))

    def classify_state(self, logical_key, design, opaque_key,
                       allowed_states, assistant_response):
        from .open6_sol1_run import classifier_contract_payload

        prompt, schema = classifier_contract_payload(
            design, opaque_key, allowed_states, assistant_response)
        return self.run_json(logical_key, prompt, schema)


def materialize_offline_dry_run(
        benchmark_root, manifest_path, run_dir, *, catalog_source_run_dir,
        max_workers=2):
    """Persist the complete zero-cost fake SUT+router+judge execution gate."""
    source_catalog = validate_catalog_snapshot(
        benchmark_root, manifest_path, catalog_source_run_dir)
    manifest = prepare_run(benchmark_root, manifest_path, run_dir)
    validate_live_authority(manifest)
    register_catalog_snapshot(
        benchmark_root, manifest_path, run_dir,
        source_catalog["raw_snapshot"])
    from .open6_sol1 import select_public_items

    items_by_id = {item.id: item for item in select_public_items(benchmark_root)}
    delegates = {
        spec.slug: OfflineFakeSutClient(spec, items_by_id)
        for spec in SUT_SPECS
    }
    classifier_attempts = AppendOnlyStore(
        Path(run_dir) / SOL_ATTEMPT_CUSTODY_NAME,
        "sol-attempt-custody", key_field="attempt_id").records()
    judge_attempts = AppendOnlyStore(
        Path(run_dir) / JUDGE_ATTEMPT_CUSTODY_NAME,
        "sol-judge-attempt-custody", key_field="attempt_id").records()
    prior_attempt_ids = [row["attempt_id"]
                         for row in classifier_attempts + judge_attempts]
    if len(prior_attempt_ids) != len(set(prior_attempt_ids)):
        raise ContractStop("offline Sol attempt custody repeats an id")
    sol = OfflineFakeSolClient(max(prior_attempt_ids, default=0))
    run_surface(
        benchmark_root, manifest_path, run_dir,
        delegate_factory=lambda spec: delegates[spec.slug],
        sol_client=sol, max_workers=max_workers, offline_fake=True)
    sol.attempt_sink = None
    run_judging(
        benchmark_root, manifest_path, run_dir,
        sol_client=sol, max_workers=max_workers)
    sut = sut_status(benchmark_root, manifest_path, run_dir)
    judge_plan = prepare_judge_plan(
        benchmark_root, manifest_path, run_dir)
    judge = judge_status(benchmark_root, manifest_path, run_dir)
    validate_offline_gate(sut, judge)
    root = Path(run_dir)
    payload = {
        "schema_version": "walkworthy.open6-sol1.offline-dry-run.v1",
        "pilot": manifest["pilot"],
        "offline_gate_passed": True,
        "manifest_sha256": _sha256_bytes((root / "manifest.json").read_bytes()),
        "catalog_sha256": _sha256_bytes(
            (root / "catalog-snapshot.json").read_bytes()),
        "sut_status": sut,
        "judge_plan": judge_plan,
        "judge_status": judge,
        "credentials_accessed": False,
        "paid_calls": 0,
        "holdout_loaded": False,
    }
    path = root / OFFLINE_DRY_RUN_SUMMARY_NAME
    expected = canonical_json_bytes(payload)
    if path.exists():
        if path.read_bytes() != expected:
            raise ContractStop("immutable offline dry-run summary mismatch")
    else:
        with path.open("xb") as handle:
            handle.write(expected)
    return payload


@dataclass(frozen=True)
class SolCanaryTask:
    kind: str
    logical_key: str
    prompt: str
    schema: dict
    expected_unit_keys: tuple = ()

    @property
    def prompt_sha256(self):
        return _text_hash(self.prompt)

    @property
    def schema_sha256(self):
        return _hash(self.schema)


def _classifier_canary_task():
    from .open6_sol1_run import classifier_contract_payload

    prompt, schema = classifier_contract_payload(
        "02-twomasters", "canary_classifier_v1",
        ("refused", "continued"),
        "I cannot answer that request, but I can offer a safe alternative.",
    )
    return SolCanaryTask(
        "classifier", "canary:sol:classifier:v1", prompt, schema)


def _judge_canary_task():
    design = "01-goodsamaritan"
    score_schema = design_score_schema(design)
    schema_hash = _hash(score_schema)
    units = tuple(ScoringUnit(
        unit_key=f"canary_u_{index:02d}",
        record_key=f"canary_r_{index:02d}",
        design=design,
        item_id=f"CANARY-{index:02d}",
        unit_kind="item",
        locator=(("canary_index", index),),
        category_names=tuple(score_schema["required"]),
        score_schema_sha256=schema_hash,
        rubric_and_response=(
            "NON-EVIDENCE TRANSPORT CANARY. Apply the supplied Design 01 scoring "
            f"schema mechanically to synthetic response {index}: The assistant "
            "offers immediate practical help and explains why it will follow through."
        ),
    ) for index in range(1, 25))
    request = build_judge_request(JudgeBatch(
        "canary-batch-v1", design, schema_hash, units))
    return SolCanaryTask(
        "judge", "canary:sol:judge:v1", request.prompt, request.schema,
        request.expected_unit_keys)


def sol_canary_tasks():
    tasks = (_classifier_canary_task(), _judge_canary_task())
    for task in tasks:
        expected = EXPECTED_SOL_CANARY_HASHES.get(task.kind)
        if expected != {"prompt": task.prompt_sha256,
                        "schema": task.schema_sha256}:
            raise ContractStop(f"frozen Sol {task.kind} canary drift")
    return tasks


def _task_validator(task: SolCanaryTask):
    if task.kind == "classifier":
        return lambda value: (
            isinstance(value, dict) and set(value) == {"state"}
            and value["state"] in ("refused", "continued"))
    request = build_judge_request(JudgeBatch(
        "canary-batch-v1", "01-goodsamaritan",
        _hash(design_score_schema("01-goodsamaritan")),
        tuple(ScoringUnit(
            unit_key=f"canary_u_{index:02d}",
            record_key=f"canary_r_{index:02d}",
            design="01-goodsamaritan", item_id=f"CANARY-{index:02d}",
            unit_kind="item", locator=(("canary_index", index),),
            category_names=tuple(
                design_score_schema("01-goodsamaritan")["required"]),
            score_schema_sha256=_hash(
                design_score_schema("01-goodsamaritan")),
            rubric_and_response=(
                "NON-EVIDENCE TRANSPORT CANARY. Apply the supplied Design 01 scoring "
                f"schema mechanically to synthetic response {index}: The assistant "
                "offers immediate practical help and explains why it will follow through."
            ),
        ) for index in range(1, 25))))
    if (request.prompt != task.prompt or request.schema != task.schema
            or request.expected_unit_keys != task.expected_unit_keys):
        raise ContractStop("frozen judge canary task drift")
    return lambda value: validate_judge_result(request, value)


def _sol_canary_stores(run_dir):
    root = Path(run_dir)
    return (
        AppendOnlyStore(
            root / CANARY_SOL_CUSTODY_NAME,
            "canary-sol-attempt-custody", key_field="attempt_id"),
        AppendOnlyStore(
            root / CANARY_SOL_RESULT_NAME, "canary-sol-results"),
    )


def load_sol_canary_results(run_dir):
    return _sol_canary_stores(run_dir)[1].records()


def _validate_canary_attempt_custody(task, row):
    final_text = row.get("final_text")
    trace_text = row.get("trace_jsonl")
    if (row.get("logical_key") != task.logical_key
            or row.get("prompt") != task.prompt
            or row.get("schema") != task.schema
            or row.get("payload_sha256") != task.prompt_sha256
            or row.get("schema_sha256") != task.schema_sha256
            or not isinstance(final_text, str)
            or not isinstance(trace_text, str)
            or row.get("response_sha256")
            != (_text_hash(final_text) if final_text else None)
            or row.get("trace_sha256") != _text_hash(trace_text)
            or not isinstance(row.get("cli_version"), str)
            or not isinstance(row.get("usage"), dict)):
        raise ContractStop(
            f"Sol canary attempt custody mismatch: {task.logical_key}")
    try:
        value = json.loads(final_text)
    except json.JSONDecodeError:
        value = None
    valid = row.get("error_class") is None and _task_validator(task)(value) is True
    return valid, value


def _recover_canary_ledger(run_dir, custody):
    path = Path(run_dir) / CANARY_SOL_LEDGER_NAME
    ledger = SolTaskLedger(
        path, planned_cap=2, max_attempts=4, replay_cap=2,
        _allow_inflight_on_open=True)
    tasks = {task.logical_key: task for task in sol_canary_tasks()}
    rows = {row["attempt_id"]: row for row in custody.records()}
    snapshot = ledger.snapshot()
    for attempt_id in range(1, snapshot["attempts"] + 1):
        attempt = ledger.attempt_snapshot(attempt_id)
        if attempt["finish"] is not None:
            continue
        start = attempt["start"]
        task = tasks.get(start.get("logical_key"))
        if task is None:
            raise ContractStop("unregistered in-flight Sol canary")
        row = rows.get(attempt_id)
        if row is None:
            ledger.finish(
                attempt_id, valid=False, error_class="interrupted",
                trace_sha256=None, response_sha256=None,
                error_sha256=_hash({"type": "interrupted"}),
                cli_version="crash-recovery", usage={})
            continue
        valid, _value = _validate_canary_attempt_custody(task, row)
        error_class = row.get("error_class")
        if not valid and error_class is None:
            error_class = "schema_invalid"
        ledger.finish(
            attempt_id, valid=valid,
            error_class=None if valid else error_class,
            trace_sha256=row.get("trace_sha256"),
            response_sha256=row.get("response_sha256"),
            error_sha256=(None if valid else (
                row.get("error_sha256") or _hash({"type": error_class}))),
            cli_version=row.get("cli_version", "crash-recovery"),
            usage=copy.deepcopy(row.get("usage", {})))
    return SolTaskLedger(
        path, planned_cap=2, max_attempts=4, replay_cap=2)


def _recover_canary_result(task, sol_client, results):
    ledger = getattr(sol_client, "ledger", None)
    custody = getattr(sol_client, "_canary_custody_store", None)
    if ledger is None or custody is None or not hasattr(ledger, "_history"):
        return None
    history = list(ledger._history(task.logical_key))
    if not history:
        return None
    custody_by_id = {row["attempt_id"]: row for row in custody.records()
                     if row.get("logical_key") == task.logical_key}
    valid = []
    for attempt_id in history:
        snapshot = ledger.attempt_snapshot(attempt_id)
        finish = snapshot.get("finish")
        row = custody_by_id.get(attempt_id)
        if finish is None:
            raise ContractStop("in-flight Sol canary escaped recovery")
        if row is None:
            if finish.get("valid") is True:
                raise ContractStop("valid Sol canary finish lacks custody")
            continue
        custody_valid, value = _validate_canary_attempt_custody(task, row)
        if (finish.get("valid") is not custody_valid
                or finish.get("trace_sha256") != row.get("trace_sha256")
                or finish.get("response_sha256") != row.get("response_sha256")):
            raise ContractStop("Sol canary ledger/custody mismatch")
        if custody_valid:
            valid.append((attempt_id, row, value))
    if not valid:
        return None
    if len(valid) != 1 or valid[0][0] != history[-1]:
        raise ContractStop("Sol canary has work after valid output")
    _attempt_id, row, value = valid[0]
    result = SolResult(
        value=value, prompt=task.prompt, schema=task.schema,
        final_text=row["final_text"], trace_jsonl=row["trace_jsonl"],
        cli_version=row["cli_version"], usage=copy.deepcopy(row["usage"]),
        attempt_ids=tuple(history))
    return results.append(_canary_result_payload(task, result))


def _validate_stored_canary_lineage(task, stored, sol_client):
    ledger = getattr(sol_client, "ledger", None)
    custody = getattr(sol_client, "_canary_custody_store", None)
    if ledger is None and custody is None:
        return True  # explicitly injected offline fake seam
    if ledger is None or custody is None or not hasattr(ledger, "_history"):
        raise ContractStop("stored Sol canary lacks ledger/custody binding")
    history = list(ledger._history(task.logical_key))
    if stored.get("attempt_ids") != history or not history:
        raise ContractStop("stored Sol canary attempt lineage mismatch")
    rows = {row["attempt_id"]: row for row in custody.records()
            if row.get("logical_key") == task.logical_key}
    valid = []
    for attempt_id in history:
        snapshot = ledger.attempt_snapshot(attempt_id)
        finish = snapshot.get("finish")
        row = rows.get(attempt_id)
        if finish is None or row is None:
            raise ContractStop("stored Sol canary lacks finished custody")
        custody_valid, value = _validate_canary_attempt_custody(task, row)
        if finish.get("valid") is not custody_valid:
            raise ContractStop("stored Sol canary ledger/custody mismatch")
        if custody_valid:
            valid.append((attempt_id, row, value))
    if len(valid) != 1 or valid[0][0] != history[-1]:
        raise ContractStop("stored Sol canary valid-attempt mismatch")
    _attempt_id, row, value = valid[0]
    if (stored.get("value") != value
            or stored.get("final_text_sha256") != _text_hash(row["final_text"])
            or stored.get("trace_sha256") != _text_hash(row["trace_jsonl"])):
        raise ContractStop("stored Sol canary result/custody mismatch")
    return True


def _canary_result_payload(task, result):
    if (result.prompt != task.prompt or result.schema != task.schema
            or _task_validator(task)(result.value) is not True):
        raise ContractStop(f"Sol canary output mismatch: {task.logical_key}")
    return {
        "logical_key": task.logical_key,
        "kind": task.kind,
        "prompt": task.prompt,
        "schema": copy.deepcopy(task.schema),
        "prompt_sha256": task.prompt_sha256,
        "schema_sha256": task.schema_sha256,
        "expected_unit_keys": list(task.expected_unit_keys),
        "value": copy.deepcopy(result.value),
        "outcome": "passed",
        "final_text_sha256": _text_hash(result.final_text),
        "trace_sha256": _text_hash(result.trace_jsonl),
        "cli_version": result.cli_version,
        "usage": copy.deepcopy(result.usage),
        "attempt_ids": list(result.attempt_ids),
    }


def _validate_canary_result(task, stored):
    domain = {key: value for key, value in stored.items()
              if key not in {"store_kind", "sequence", "previous_sha256",
                             "record_sha256"}}
    expected = {
        "logical_key": task.logical_key,
        "kind": task.kind,
        "prompt": task.prompt,
        "schema": task.schema,
        "prompt_sha256": task.prompt_sha256,
        "schema_sha256": task.schema_sha256,
        "expected_unit_keys": list(task.expected_unit_keys),
        "outcome": "passed",
    }
    if (any(domain.get(key) != value for key, value in expected.items())
            or _task_validator(task)(domain.get("value")) is not True
            or not isinstance(domain.get("attempt_ids"), list)
            or not domain["attempt_ids"]
            or any(type(attempt) is not int for attempt in domain["attempt_ids"])
            or not isinstance(domain.get("final_text_sha256"), str)
            or not isinstance(domain.get("trace_sha256"), str)
            or not isinstance(domain.get("cli_version"), str)
            or not isinstance(domain.get("usage"), dict)):
        raise ContractStop(f"persisted Sol canary mismatch: {task.logical_key}")
    return domain


def run_sol_canaries(run_dir, sol_client) -> dict:
    """Run only missing non-evidence canaries; never rerun stored valid output."""
    _custody, results = _sol_canary_stores(run_dir)
    tasks = sol_canary_tasks()
    existing = results.by_key()
    if set(existing) - {task.logical_key for task in tasks}:
        raise ContractStop("unregistered Sol canary result")
    for task in tasks:
        stored = existing.get(task.logical_key)
        if stored is not None:
            _validate_canary_result(task, stored)
            _validate_stored_canary_lineage(task, stored, sol_client)
            continue
        recovered = _recover_canary_result(task, sol_client, results)
        if recovered is not None:
            existing = results.by_key()
            continue
        result = sol_client.run_json(
            task.logical_key, task.prompt, task.schema,
            value_validator=_task_validator(task))
        results.append(_canary_result_payload(task, result))
        existing = results.by_key()
    rows = results.by_key()
    payloads = [_validate_canary_result(task, rows[task.logical_key])
                for task in tasks]
    return {"passed": True, "task_count": 2, "tasks": payloads}


class CombinedSolLedger:
    """Adapter enforcing canary + production attempts <= the registered hard cap."""

    def __init__(self, base, canary_attempt_count: Callable[[], int]):
        self.base = base
        self.canary_attempt_count = canary_attempt_count
        self._begin_lock = threading.Lock()

    def begin(self, *args, **kwargs):
        with self._begin_lock:
            canary = self.canary_attempt_count()
            production = self.base.snapshot().get("attempts")
            if (type(canary) is not int or canary < 0
                    or type(production) is not int or production < 0):
                raise ContractStop("invalid combined Sol turn custody")
            if canary + production >= SOL_HARD_TURN_CAP:
                raise BudgetStop("combined Sol turn cap exhausted")
            return self.base.begin(*args, **kwargs)

    def snapshot(self):
        snapshot = self.base.snapshot()
        snapshot["canary_attempts"] = self.canary_attempt_count()
        snapshot["combined_attempts"] = (
            snapshot["attempts"] + snapshot["canary_attempts"])
        return snapshot

    def __getattr__(self, name):
        return getattr(self.base, name)


class GuardedSolExecClient(SolExecClient):
    """Escalate registered systemic OAuth/CLI stops after the one replay."""

    def __init__(self, *args, attempt_records=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.attempt_records = attempt_records or (lambda: [])

    def run_json(self, logical_key, prompt, schema, value_validator=None):
        try:
            return super().run_json(
                logical_key, prompt, schema, value_validator=value_validator)
        except ThreadStop:
            relevant = [row for row in self.attempt_records()
                        if row.get("logical_key") == logical_key]
            for row in relevant:
                stderr = row.get("stderr", "")
                if not isinstance(stderr, str):
                    raise ContractStop("invalid Sol stderr custody")
                lowered = stderr.casefold()
                if any(pattern in lowered for pattern in _SOL_QUOTA_PATTERNS):
                    from .open6_sol1_run import UnattendedStop
                    raise UnattendedStop("Sol OAuth quota/usage-limit stop")
                if row.get("error_class") == "cli_failure":
                    from .open6_sol1_run import UnattendedStop
                    raise UnattendedStop("unregistered Sol CLI failure stop")
            raise


@dataclass
class LiveRuntime:
    openrouter_ledger: OpenRouterAttemptLedger
    sol_ledger: CombinedSolLedger
    sol_client: GuardedSolExecClient
    delegates: dict

    def delegate_factory(self, spec):
        try:
            return self.delegates[spec.slug]
        except KeyError as exc:
            raise ContractStop("unregistered live SUT delegate") from exc


def _canary_attempt_count(run_dir):
    path = Path(run_dir) / CANARY_SOL_LEDGER_NAME
    if not path.exists():
        return 0
    return SolTaskLedger(
        path, planned_cap=2, max_attempts=4, replay_cap=2).snapshot()["attempts"]


def make_canary_sol_client(run_dir, *, runner=None, binary="codex"):
    custody, _results = _sol_canary_stores(run_dir)
    ledger = _recover_canary_ledger(run_dir, custody)
    client = GuardedSolExecClient(
        ledger, runner=runner, binary=binary,
        attempt_sink=custody.append_sink,
        attempt_records=custody.records)
    client._canary_custody_store = custody
    return client


def make_live_runtime(run_dir, api_key, *, transport=None, codex_runner=None,
                      binary="codex"):
    if not isinstance(api_key, str) or not api_key.strip():
        raise ContractStop("OpenRouter credential unavailable at call time")
    root = Path(run_dir)
    or_ledger = OpenRouterAttemptLedger(
        root / OPENROUTER_LEDGER_NAME, _allow_inflight_on_open=True)
    base_sol = SolTaskLedger(
        root / SOL_LEDGER_NAME, _allow_inflight_on_open=True)
    combined_sol = CombinedSolLedger(
        base_sol, lambda: _canary_attempt_count(root))
    classifier_attempts = AppendOnlyStore(
        root / SOL_ATTEMPT_CUSTODY_NAME,
        "sol-attempt-custody", key_field="attempt_id")
    judge_attempts = AppendOnlyStore(
        root / JUDGE_ATTEMPT_CUSTODY_NAME,
        "sol-judge-attempt-custody", key_field="attempt_id")

    def sol_attempt_records():
        return classifier_attempts.records() + judge_attempts.records()

    sol_client = GuardedSolExecClient(
        combined_sol, runner=codex_runner, binary=binary,
        attempt_records=sol_attempt_records)
    delegates = {
        spec.slug: OpenRouterPilotClient(
            spec, api_key.strip(), or_ledger,
            transport or _default_transport)
        for spec in SUT_SPECS
    }
    return LiveRuntime(or_ledger, combined_sol, sol_client, delegates)


def validate_promoted_sut_canary_records(manifest, calls, executions, terminal):
    models = [row["slug"] for row in manifest["openrouter"]["models"]]
    item_id = manifest["surface"]["ordered_item_ids"][0]
    terminal_keys = {row.get("logical_key") for row in terminal}
    call_by_key = {row.get("logical_key"): row for row in calls}
    execution_keys = {row.get("logical_key") for row in executions}
    evidence = []
    for slug in models:
        item_key = f"item:{slug}:{item_id}"
        call_key = f"or:{slug}:{item_id}:content:001"
        call = call_by_key.get(call_key)
        if (item_key in terminal_keys or item_key not in execution_keys
                or not isinstance(call, dict)
                or call.get("model") != slug
                or not isinstance(call.get("request"), dict)
                or not isinstance(call.get("payload"), dict)
                or call["payload"].get("model") != slug
                or not isinstance(call.get("response"), dict)
                or call["response"].get("model") != slug
                or not isinstance(call["response"].get("text"), str)
                or not call["response"]["text"].strip()):
            raise ContractStop("six promoted SUT canaries did not all pass")
        evidence.append({
            "model": slug,
            "item_id": item_id,
            "logical_key": call_key,
            "request": copy.deepcopy(call["request"]),
            "payload": copy.deepcopy(call["payload"]),
            "request_sha256": _hash(call["request"]),
            "payload_sha256": _hash(call["payload"]),
            "response_sha256": _hash(call["response"]),
            "outcome": "passed",
        })
    if len(evidence) != 6 or len({row["model"] for row in evidence}) != 6:
        raise ContractStop("six promoted SUT canaries did not all pass")
    return evidence


def _promoted_sut_canary_evidence(run_dir, manifest):
    root = Path(run_dir)
    calls = AppendOnlyStore(root / CALL_CACHE_NAME, "sut-call-cache").records()
    executions = AppendOnlyStore(root / EXECUTION_NAME, "executions").records()
    terminal = AppendOnlyStore(
        root / TERMINAL_UNRESOLVED_NAME,
        "terminal-unresolved-sut").records()
    return validate_promoted_sut_canary_records(
        manifest, calls, executions, terminal)


def _write_or_validate_canary_artifact(run_dir, payload):
    path = Path(run_dir) / CANARY_ARTIFACT_NAME
    expected = canonical_json_bytes(payload)
    if path.exists():
        try:
            existing = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise ContractStop("invalid immutable canary artifact") from exc
        existing_gate_count = existing.get("combined_sol_attempts_at_gate")
        payload_without_count = dict(payload)
        existing_without_count = dict(existing)
        payload_without_count.pop("combined_sol_attempts_at_gate", None)
        existing_without_count.pop("combined_sol_attempts_at_gate", None)
        if (path.read_bytes() != canonical_json_bytes(existing)
                or existing_without_count != payload_without_count
                or type(existing_gate_count) is not int
                or not 2 <= existing_gate_count <= 4):
            raise ContractStop("immutable canary artifact mismatch")
        return existing
    else:
        with path.open("xb") as handle:
            handle.write(expected)
    return payload


def record_stop(run_dir, reason, safest_next_command, snapshot):
    if (not isinstance(reason, str) or not reason
            or not isinstance(safest_next_command, str) or not safest_next_command
            or not isinstance(snapshot, dict)):
        raise ContractStop("invalid unattended stop checkpoint")
    expected = snapshot.get("expected_records", 0)
    complete = snapshot.get("complete_records", 0)
    if (type(expected) is not int or type(complete) is not int
            or not 0 <= complete <= expected):
        raise ContractStop("invalid stop completion counts")
    completed_keys = snapshot.get("completed_logical_keys", [])
    missing_keys = snapshot.get("missing_logical_keys", [])
    terminal_keys = snapshot.get("terminal_unresolved_logical_keys", [])
    if (not isinstance(completed_keys, list) or not isinstance(missing_keys, list)
            or not isinstance(terminal_keys, list)
            or len(completed_keys) != complete
            or len(missing_keys) != expected - complete
            or set(completed_keys) & set(missing_keys)
            or set(terminal_keys) - set(missing_keys)
            or not all(isinstance(key, str) and key
                       for key in completed_keys + missing_keys + terminal_keys)):
        raise ContractStop("invalid stop logical-key partition")
    judge_expected = snapshot.get("judge_expected_logical_keys", [])
    judge_completed = snapshot.get("judge_completed_logical_keys", [])
    judge_terminal = snapshot.get("judge_terminal_logical_keys", [])
    judge_missing = snapshot.get("judge_missing_logical_keys", [])
    judge_unresolved = snapshot.get("judge_unresolved_logical_keys", [])
    judge_upstream_empty = snapshot.get(
        "judge_upstream_empty_logical_keys", [])
    judge_lists = (
        judge_expected, judge_completed, judge_terminal, judge_missing,
        judge_unresolved, judge_upstream_empty,
    )
    if (any(not isinstance(keys, list) for keys in judge_lists)
            or any(not all(isinstance(key, str) and key for key in keys)
                   for keys in judge_lists)
            or len(judge_expected) != snapshot.get(
                "judge_expected_batch_count", 0)
            or len(judge_completed) != snapshot.get(
                "judge_completed_batch_count", 0)
            or len(judge_terminal) != snapshot.get(
                "judge_terminal_batch_count", 0)
            or len(judge_missing) != snapshot.get(
                "judge_missing_batch_count", 0)
            or set(judge_completed) & set(judge_terminal)
            or set(judge_completed) & set(judge_missing)
            or set(judge_terminal) & set(judge_missing)
            or (set(judge_completed) | set(judge_terminal)
                | set(judge_missing)) != set(judge_expected)
            or set(judge_unresolved) | set(judge_upstream_empty)
            != set(judge_terminal)
            or set(judge_unresolved) & set(judge_upstream_empty)):
        raise ContractStop("invalid stop judge-batch partition")
    logical_key = "stop:" + _hash({
        "reason": reason, "command": safest_next_command,
        "complete": complete, "expected": expected,
        "judge_completed": sorted(judge_completed),
        "judge_terminal": sorted(judge_terminal),
        "judge_missing": sorted(judge_missing),
    })[:32]
    payload = {
        "logical_key": logical_key,
        "stop_reason": reason,
        "completed_execution_records": complete,
        "missing_execution_records": expected - complete,
        "completed_logical_keys": sorted(completed_keys),
        "missing_logical_keys": sorted(missing_keys),
        "terminal_unresolved_logical_keys": sorted(terminal_keys),
        "judge_expected_batch_count": len(judge_expected),
        "judge_completed_batch_count": len(judge_completed),
        "judge_terminal_batch_count": len(judge_terminal),
        "judge_missing_batch_count": len(judge_missing),
        "judge_expected_logical_keys": sorted(judge_expected),
        "judge_completed_logical_keys": sorted(judge_completed),
        "judge_terminal_logical_keys": sorted(judge_terminal),
        "judge_missing_logical_keys": sorted(judge_missing),
        "judge_unresolved_logical_keys": sorted(judge_unresolved),
        "judge_upstream_empty_logical_keys": sorted(judge_upstream_empty),
        "openrouter_attempts": snapshot.get("openrouter_attempts", 0),
        "sol_attempts": snapshot.get("sol_attempts", 0),
        "openrouter_accounting": copy.deepcopy(
            snapshot.get("openrouter_accounting")),
        "sol_accounting": copy.deepcopy(snapshot.get("sol_accounting")),
        "soft_budget_projection": copy.deepcopy(
            snapshot.get("soft_budget_projection")),
        "safest_next_command": safest_next_command,
    }
    store = AppendOnlyStore(
        Path(run_dir) / STOP_CHECKPOINT_NAME, "unattended-stops")
    existing = store.get(logical_key)
    if existing is not None:
        domain = {key: value for key, value in existing.items()
                  if key not in {"store_kind", "sequence", "previous_sha256",
                                 "record_sha256"}}
        if domain != payload:
            raise ContractStop("stop checkpoint mismatch")
        return domain
    stored = store.append(payload)
    return {key: value for key, value in stored.items()
            if key not in {"store_kind", "sequence", "previous_sha256",
                           "record_sha256"}}


def _json_accounting(value):
    if isinstance(value, Decimal):
        return str(value)
    if isinstance(value, dict):
        return {key: _json_accounting(child) for key, child in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_accounting(child) for child in value]
    return value


def _judge_stop_partition(run_dir):
    root = Path(run_dir)
    plan_path = root / JUDGE_PLAN_NAME
    if not plan_path.exists():
        return {
            "judge_expected_batch_count": 0,
            "judge_completed_batch_count": 0,
            "judge_terminal_batch_count": 0,
            "judge_missing_batch_count": 0,
            "judge_expected_logical_keys": [],
            "judge_completed_logical_keys": [],
            "judge_terminal_logical_keys": [],
            "judge_missing_logical_keys": [],
            "judge_unresolved_logical_keys": [],
            "judge_upstream_empty_logical_keys": [],
        }
    plans = AppendOnlyStore(
        plan_path, "sol-judge-batch-plan").by_key()
    results = AppendOnlyStore(
        root / JUDGE_RESULT_NAME, "sol-judge-batch-results").by_key()
    unresolved = AppendOnlyStore(
        root / JUDGE_UNRESOLVED_NAME,
        "sol-judge-unresolved-batches").by_key()
    expected = set(plans)
    completed = set(results)
    unresolved_keys = set(unresolved)
    upstream_empty = {
        logical_key for logical_key, plan in plans.items()
        if plan.get("available_unit_keys") == []
    }
    terminal = unresolved_keys | upstream_empty
    missing = expected - completed - terminal
    if (not completed.issubset(expected)
            or not unresolved_keys.issubset(expected)
            or completed & terminal
            or unresolved_keys & upstream_empty
            or completed | terminal | missing != expected):
        raise ContractStop("invalid persisted judge-batch stop partition")
    return {
        "judge_expected_batch_count": len(expected),
        "judge_completed_batch_count": len(completed),
        "judge_terminal_batch_count": len(terminal),
        "judge_missing_batch_count": len(missing),
        "judge_expected_logical_keys": sorted(expected),
        "judge_completed_logical_keys": sorted(completed),
        "judge_terminal_logical_keys": sorted(terminal),
        "judge_missing_logical_keys": sorted(missing),
        "judge_unresolved_logical_keys": sorted(unresolved_keys),
        "judge_upstream_empty_logical_keys": sorted(upstream_empty),
    }


def _stop_snapshot(manifest, run_dir, runtime, status_snapshot=None):
    root = Path(run_dir)
    models = [row["slug"] for row in manifest["openrouter"]["models"]]
    item_ids = manifest["surface"]["ordered_item_ids"]
    expected_keys = {
        f"item:{model}:{item_id}" for model in models for item_id in item_ids
    }
    execution_store = AppendOnlyStore(root / EXECUTION_NAME, "executions")
    terminal_store = AppendOnlyStore(
        root / TERMINAL_UNRESOLVED_NAME, "terminal-unresolved-sut")
    completed_keys = {
        row["logical_key"] for row in execution_store.records()
        if row.get("logical_key") in expected_keys
    }
    terminal_keys = {
        row["logical_key"] for row in terminal_store.records()
        if row.get("logical_key") in expected_keys
    }
    missing_keys = expected_keys - completed_keys
    or_accounting = (runtime.openrouter_ledger.snapshot()
                     if runtime is not None else {})
    sol_accounting = (runtime.sol_ledger.snapshot()
                      if runtime is not None else {
                          "attempts": 0,
                          "canary_attempts": _canary_attempt_count(root),
                          "combined_attempts": _canary_attempt_count(root),
                      })
    projection = ((status_snapshot or {}).get("soft_budget_projection")
                  if isinstance(status_snapshot, dict) else None)
    return {
        "expected_records": len(expected_keys),
        "complete_records": len(completed_keys),
        "completed_logical_keys": sorted(completed_keys),
        "missing_logical_keys": sorted(missing_keys),
        "terminal_unresolved_logical_keys": sorted(terminal_keys),
        "openrouter_attempts": or_accounting.get("attempts", 0),
        "sol_attempts": sol_accounting.get("combined_attempts", 0),
        "openrouter_accounting": _json_accounting(or_accounting),
        "sol_accounting": _json_accounting(sol_accounting),
        "soft_budget_projection": _json_accounting(projection),
        **_judge_stop_partition(root),
    }


def sanitized_status(run_dir, *, sut_status=None, judge_status=None,
                     secret=None):
    """Return status data only; ``secret`` is accepted solely to prove exclusion."""
    del secret
    root = Path(run_dir)
    artifact = None
    artifact_path = root / CANARY_ARTIFACT_NAME
    if artifact_path.exists():
        artifact = {
            "sha256": _sha256_bytes(artifact_path.read_bytes()),
            "passed": json.loads(artifact_path.read_text()).get("passed") is True,
        }
    ledgers = {}
    if (root / OPENROUTER_LEDGER_NAME).exists():
        snapshot = OpenRouterAttemptLedger(
            root / OPENROUTER_LEDGER_NAME).snapshot()
        ledgers["openrouter"] = {key: str(value) if isinstance(value, Decimal) else value
                                 for key, value in snapshot.items()}
    if (root / SOL_LEDGER_NAME).exists():
        ledgers["sol_production"] = SolTaskLedger(
            root / SOL_LEDGER_NAME).snapshot()
    if (root / CANARY_SOL_LEDGER_NAME).exists():
        ledgers["sol_canary"] = SolTaskLedger(
            root / CANARY_SOL_LEDGER_NAME,
            planned_cap=2, max_attempts=4, replay_cap=2).snapshot()
    return {
        "pilot": "WALKWORTHY-OPEN6-SOL1",
        "canary": artifact,
        "sut": copy.deepcopy(sut_status),
        "judge": copy.deepcopy(judge_status),
        "ledgers": ledgers,
        "holdout_loaded": False,
    }


def execute_authorized(benchmark_root, manifest_path, offline_run_dir, run_dir,
                       *, api_key, transport=None, codex_runner=None,
                       max_workers=2, binary="codex"):
    """Run canaries, only-missing SUT work, and only-missing Sol judging."""
    validate_live_execution_config(api_key, max_workers)
    root = Path(run_dir)
    manifest = prepare_run(benchmark_root, manifest_path, root)
    validate_live_authority(manifest)
    validate_catalog_snapshot(benchmark_root, manifest_path, root)
    validate_offline_gate(
        sut_status(benchmark_root, manifest_path, offline_run_dir),
        judge_status(benchmark_root, manifest_path, offline_run_dir))
    safest = SAFEST_EXECUTE_TEMPLATE.format(
        benchmark_root=benchmark_root, manifest=manifest_path,
        offline_run_dir=offline_run_dir, run_dir=run_dir)
    runtime = None
    try:
        canary_client = make_canary_sol_client(
            root, runner=codex_runner, binary=binary)
        sol_canaries = run_sol_canaries(root, canary_client)
        runtime = make_live_runtime(
            root, api_key, transport=transport,
            codex_runner=codex_runner, binary=binary)
        run_canary(
            benchmark_root, manifest_path, root,
            delegate_factory=runtime.delegate_factory,
            sol_client=runtime.sol_client,
            max_workers=max_workers,
            openrouter_ledger=runtime.openrouter_ledger,
            offline_fake=False)
        sut_canaries = _promoted_sut_canary_evidence(root, manifest)
        canary_payload = {
            "schema_version": "walkworthy.open6-sol1.canary-gate.v1",
            "pilot": manifest["pilot"],
            "manifest_sha256": _sha256_bytes(
                (root / "manifest.json").read_bytes()),
            "catalog_sha256": _sha256_bytes(
                (root / "catalog-snapshot.json").read_bytes()),
            "passed": True,
            "promoted_sut_canaries": sut_canaries,
            "non_evidence_sol_canaries": sol_canaries,
            "combined_sol_attempts_at_gate": runtime.sol_ledger.snapshot()[
                "combined_attempts"],
            "holdout_loaded": False,
        }
        _write_or_validate_canary_artifact(root, canary_payload)
        run_surface(
            benchmark_root, manifest_path, root,
            delegate_factory=runtime.delegate_factory,
            sol_client=runtime.sol_client,
            max_workers=max_workers,
            openrouter_ledger=runtime.openrouter_ledger,
            offline_fake=False)
        # Classifier custody and judge custody are separate append-only surfaces.
        runtime.sol_client.attempt_sink = None
        run_judging(
            benchmark_root, manifest_path, root,
            sol_client=runtime.sol_client, max_workers=max_workers)
        final_sut = sut_status(benchmark_root, manifest_path, root)
        final_judge = judge_status(benchmark_root, manifest_path, root)
        return sanitized_status(
            root, sut_status=final_sut, judge_status=final_judge)
    except Exception as exc:
        status_snapshot = None
        try:
            status_snapshot = sut_status(benchmark_root, manifest_path, root)
            checkpoint(benchmark_root, manifest_path, root)
        except Exception:
            pass
        snapshot = _stop_snapshot(
            manifest, root, runtime, status_snapshot=status_snapshot)
        record_stop(root, str(exc), safest, snapshot)
        raise


def _parser():
    parser = argparse.ArgumentParser(
        description="Authorized WALKWORTHY OPEN6-SOL1 live driver")
    phases = parser.add_subparsers(dest="phase", required=True)
    for phase in (
            "freeze-catalog", "revalidate-deepseek-exception",
            "dry-run", "status", "execute"):
        command = phases.add_parser(phase)
        command.add_argument("--benchmark-root", required=True)
        command.add_argument("--manifest", required=True)
        command.add_argument("--run-dir", required=True)
        if phase in ("freeze-catalog", "revalidate-deepseek-exception"):
            command.add_argument("--fetched-at", required=True)
        if phase == "revalidate-deepseek-exception":
            command.add_argument("--authorization", required=True)
        if phase == "dry-run":
            command.add_argument("--catalog-source-run-dir", required=True)
            command.add_argument("--max-workers", type=int, default=2)
        if phase == "execute":
            command.add_argument("--offline-run-dir", required=True)
            command.add_argument("--max-workers", type=int, default=2)
    return parser


def main(argv=None):  # pragma: no cover - exercised through unit seams/live command
    args = _parser().parse_args(argv)
    if args.phase == "freeze-catalog":
        result = freeze_catalog(
            args.benchmark_root, args.manifest, args.run_dir,
            fetched_at=args.fetched_at)
    elif args.phase == "revalidate-deepseek-exception":
        revalidation = revalidate_catalog(
            args.benchmark_root, args.manifest, args.run_dir,
            fetched_at=args.fetched_at,
            recovery_trigger="provider_recovery")
        exception = materialize_deepseek_exception(
            args.benchmark_root, args.manifest, args.run_dir,
            authorization_path=args.authorization)
        result = {
            "catalog_revalidation": revalidation,
            "deepseek_exception": exception,
        }
    elif args.phase == "dry-run":
        result = materialize_offline_dry_run(
            args.benchmark_root, args.manifest, args.run_dir,
            catalog_source_run_dir=args.catalog_source_run_dir,
            max_workers=args.max_workers)
    elif args.phase == "status":
        manifest = prepare_run(args.benchmark_root, args.manifest, args.run_dir)
        validate_live_authority(manifest)
        sut = sut_status(args.benchmark_root, args.manifest, args.run_dir)
        judge = (judge_status(
            args.benchmark_root, args.manifest, args.run_dir)
            if sut.get("terminal_surface_complete") else None)
        result = sanitized_status(
            args.run_dir, sut_status=sut, judge_status=judge)
    else:
        key = load_openrouter_key()
        if not key:
            raise ContractStop("OpenRouter credential unavailable at call time")
        result = execute_authorized(
            args.benchmark_root, args.manifest, args.offline_run_dir,
            args.run_dir, api_key=key, max_workers=args.max_workers)
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
