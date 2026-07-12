"""Resumable access -> canary -> smoke orchestration for public episodes only."""
from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path

from . import contracts, executor
from .evidence import EvidenceStore
from .report import build_report
from .selection import build_canary_selection


DEFAULT_MODELS = tuple(contracts.load_profile()["models"])
_FAILURE_FIELDS = {
    "artifact_version", "kind", "status", "purpose", "provenance",
    "measurement_ready", "public_qualification_evidence", "model_alias",
    "item_id", "attempt", "binding", "error_code", "error_message",
    "failure_evidence",
    "authorizes_private_execution", "authorizes_calibration",
    "authorizes_freeze",
}


def _safe_error_message(error: Exception) -> str:
    message = str(error)
    try:
        contracts.assert_artifact_safe(message)
    except ValueError:
        return "error detail redacted by credential guard"
    return message


class _AccessFailureError(ValueError):
    """Access-phase failure carrying the exact canonical paid-call boundary."""

    def __init__(self, error: Exception, failure_evidence: dict):
        super().__init__(_safe_error_message(error))
        self.original_error_code = type(error).__name__
        self.failure_evidence = failure_evidence


def _load_json(path: Path):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        raise ValueError(f"bank artifact is not readable strict JSON: {path}") from None


def _slug(alias: str) -> str:
    if alias.count("/") != 1:
        raise ValueError("model alias must be author/model")
    return alias.replace("/", "--")


def _bank_state(bank_root: Path) -> dict:
    bank_root = Path(bank_root).resolve()
    public_path = bank_root / "seeds_public.yaml"
    truth_path = bank_root / "sidecar" / "ground_truth.json"
    public = _load_json(public_path)
    full_truth = _load_json(truth_path)
    if not isinstance(public, list) or len(public) != 30:
        raise ValueError("qualification requires exactly 30 public episodes")
    ids = [row.get("id") for row in public if isinstance(row, dict)]
    if len(ids) != 30 or len(set(ids)) != 30 or any(
            row.get("split") != "public" for row in public):
        raise ValueError("public episode scope/IDs are invalid")
    truth = {}
    for item_id in ids:
        row = full_truth.get(item_id)
        if not isinstance(row, dict) or row.get("split") != "public":
            raise ValueError("public ground truth coverage is incomplete")
        truth[item_id] = row
    public_by_id = {row["id"]: row for row in public}
    staged_tool_schemas = {}
    for item_id in ids:
        try:
            digest = executor.tool_schema_sha256(
                public_by_id[item_id], truth[item_id]
            )
            staged_tool_schemas[item_id] = contracts.assert_sha256(
                digest, f"staged tool contract {item_id}"
            )
        except (KeyError, TypeError, ValueError) as error:
            raise ValueError(
                f"public staged tool contract incomplete for {item_id}: {error}"
            ) from None
    bank_sha = contracts.sha256_value({"episodes": public, "truth": truth})
    return {
        "bank_root": bank_root, "public": public, "episodes": public_by_id,
        "truth": truth, "public_item_ids": ids, "bank_sha256": bank_sha,
        "staged_tool_schema_sha256": staged_tool_schemas,
        "source_hashes": {
            "seeds_public": contracts.sha256_file(public_path),
            "ground_truth": contracts.sha256_file(truth_path),
            "staged_tool_contracts": contracts.sha256_value(staged_tool_schemas),
        },
    }


def _code_hashes(bank_root: Path) -> dict:
    pilot_root = Path(__file__).resolve().parent
    return {
        "profile": contracts.sha256_value(contracts.load_profile()),
        "pilot_contracts": contracts.sha256_file(pilot_root / "contracts.py"),
        "openrouter_transport": contracts.sha256_file(pilot_root / "openrouter.py"),
        "runner": contracts.sha256_file(Path(__file__)),
        "payload_contract": contracts.sha256_file(bank_root / "lib" / "payloads.py"),
        "path_classifier": contracts.sha256_file(
            bank_root / "scorers" / "path_classifier.py"
        ),
        "followthrough": contracts.sha256_file(
            bank_root / "scorers" / "followthrough.py"
        ),
        "executor": contracts.sha256_file(Path(executor.__file__)),
    }


class QualificationRunner:
    """One immutable-profile, public-only CROSSROADS qualification root."""

    def __init__(self, root: Path, *, bank_root: Path, client):
        self.root = Path(root).expanduser().absolute()
        self.bank = _bank_state(bank_root)
        self.client = client
        self.store = EvidenceStore(self.root)
        self.manifest = _load_json(self.root / "manifest.json")
        self.canary_selection = _load_json(self.root / "canary_selection.json")
        self._validate_current_bindings()

    @classmethod
    def create(cls, root: Path, *, bank_root: Path, client,
               model_aliases=None, provenance=contracts.PROVENANCE_MOCK,
               execution_mode=executor.STAGED_MODE):
        if provenance not in {contracts.PROVENANCE_MOCK, contracts.PROVENANCE_LIVE}:
            raise ValueError("qualification provenance is invalid")
        if provenance == contracts.PROVENANCE_LIVE and getattr(
                client, "live_transport", False) is not True:
            raise ValueError("live provenance requires the production OpenRouter client")
        if execution_mode not in {executor.STAGED_MODE, executor.DIAGNOSTIC_MODE}:
            raise ValueError("execution mode is invalid")
        aliases = list(DEFAULT_MODELS if model_aliases is None else model_aliases)
        if not aliases or len(aliases) != len(set(aliases)):
            raise ValueError("model aliases must be non-empty and unique")
        models = [contracts.resolve_model(alias) for alias in aliases]
        bank = _bank_state(bank_root)
        hashes = {"bank": bank["bank_sha256"], **bank["source_hashes"],
                  **_code_hashes(bank["bank_root"])}
        canary = build_canary_selection(
            bank["public"], bank["truth"], bank_sha256=bank["bank_sha256"]
        )
        manifest = {
            "manifest_version": "crossroads-public-qualification-v6",
            "purpose": "public qualification",
            "provenance": provenance,
            "measurement_ready": False,
            "public_qualification_evidence": True,
            "execution_mode": execution_mode,
            "canonical_e_measurement": False,
            "issues_live_judges": False,
            "authorizes_model_ranking": False,
            "profile_id": contracts.load_profile()["profile_id"],
            "models": aliases,
            "expected_snapshots": {
                row["alias"]: row["expected_snapshot"] for row in models
            },
            "public_item_ids": bank["public_item_ids"],
            "canary_item_ids": canary["item_ids"],
            "hashes": hashes,
            "max_attempts": 3,
            "authorizes_private_execution": False,
            "authorizes_calibration": False,
            "authorizes_freeze": False,
        }
        EvidenceStore.create(root, manifest, canary)
        return cls(root, bank_root=bank_root, client=client)

    @classmethod
    def open(cls, root: Path, *, bank_root: Path, client):
        return cls(root, bank_root=bank_root, client=client)

    def _validate_current_bindings(self):
        manifest = self.manifest
        profile = contracts.load_profile()
        if manifest.get("manifest_version") != (
                "crossroads-public-qualification-v6"):
            raise ValueError("qualification manifest version differs")
        if manifest.get("profile_id") != profile["profile_id"]:
            raise ValueError("qualification profile identity differs")
        if manifest.get("purpose") != "public qualification" or manifest.get(
                "measurement_ready") is not False:
            raise ValueError("qualification manifest purpose/measurement label differs")
        if manifest.get("canonical_e_measurement") is not False or manifest.get(
                "issues_live_judges") is not False:
            raise ValueError("qualification manifest path-only scope differs")
        if manifest.get("public_item_ids") != self.bank["public_item_ids"]:
            raise ValueError("qualification public bank IDs changed")
        if manifest.get("canary_item_ids") != self.canary_selection.get("item_ids"):
            raise ValueError("qualification canary binding changed")
        if manifest.get("max_attempts") != 3:
            raise ValueError("qualification retry ceiling changed")
        current = {"bank": self.bank["bank_sha256"], **self.bank["source_hashes"],
                   **_code_hashes(self.bank["bank_root"])}
        if manifest.get("hashes") != current:
            raise ValueError("qualification bank/profile/tool/scorer hashes changed")
        for alias in manifest.get("models", []):
            model = contracts.resolve_model(alias)
            if manifest["expected_snapshots"].get(alias) != model["expected_snapshot"]:
                raise ValueError("qualification model snapshot binding changed")
        for flag in (
            "authorizes_private_execution", "authorizes_calibration",
            "authorizes_freeze", "authorizes_model_ranking",
        ):
            if manifest.get(flag) is not False:
                raise ValueError("qualification authorization flag changed")

    def _phase_complete(self, phase: str) -> bool:
        return any(
            row["event"] == f"phase_complete:{phase}"
            for row in self.store.read_journal()
        )

    def _request_binding(self, item_id: str) -> dict:
        episode = self.bank["episodes"][item_id]
        return {
            "bank_sha256": self.manifest["hashes"]["bank"],
            "public_item_sha256": contracts.sha256_value(episode),
            "profile_sha256": self.manifest["hashes"]["profile"],
            "tool_schema_sha256": self.bank[
                "staged_tool_schema_sha256"
            ][item_id],
            "scorer_sha256": {
                "path_classifier": self.manifest["hashes"]["path_classifier"],
                "followthrough": self.manifest["hashes"]["followthrough"],
            },
        }

    def _safe_failure(self, *, kind: str, alias: str, attempt: int,
                      item_id: str | None, binding: dict,
                      error: Exception) -> dict:
        message = _safe_error_message(error)
        return {
            "artifact_version": "crossroads-qualification-attempt-v2",
            "kind": kind, "status": "failed", "purpose": "public qualification",
            "provenance": self.manifest["provenance"],
            "measurement_ready": False, "public_qualification_evidence": True,
            "model_alias": alias, "item_id": item_id, "attempt": attempt,
            "binding": deepcopy(binding),
            "error_code": getattr(
                error, "original_error_code", type(error).__name__
            ),
            "error_message": message,
            "failure_evidence": deepcopy(
                getattr(error, "failure_evidence", None)
            ),
            "authorizes_private_execution": False,
            "authorizes_calibration": False, "authorizes_freeze": False,
        }

    def _attempt_binding(self, *, kind: str, alias: str,
                         item_id: str | None, attempt: int) -> dict:
        if kind == "access":
            if item_id is not None:
                raise ValueError("access attempt cannot bind an item")
            return deepcopy(self._access_request(
                contracts.resolve_model(alias), attempt
            )["binding"])
        if kind == "episode":
            if item_id not in self.bank["episodes"]:
                raise ValueError("episode attempt item is outside the public bank")
            return self._request_binding(item_id)
        raise ValueError("unknown attempt kind")

    def _validate_failure(self, payload: dict, *, kind: str,
                          alias: str, item_id: str | None,
                          attempt: int) -> bool:
        try:
            if not isinstance(payload, dict) or set(payload) != _FAILURE_FIELDS:
                return False
            if (
                payload.get("artifact_version")
                != "crossroads-qualification-attempt-v2"
                or payload.get("kind") != kind
                or payload.get("status") != "failed"
                or payload.get("purpose") != "public qualification"
                or payload.get("provenance") != self.manifest["provenance"]
                or payload.get("measurement_ready") is not False
                or payload.get("public_qualification_evidence") is not True
                or payload.get("model_alias") != alias
                or alias not in self.manifest["models"]
                or payload.get("item_id") != item_id
                or payload.get("attempt") != attempt
                or type(attempt) is not int or not 1 <= attempt <= 3
                or payload.get("binding") != self._attempt_binding(
                    kind=kind, alias=alias, item_id=item_id, attempt=attempt
                )
                or not isinstance(payload.get("error_code"), str)
                or not payload["error_code"]
                or not isinstance(payload.get("error_message"), str)
                or not payload["error_message"]
            ):
                return False
            evidence = payload.get("failure_evidence")
            if kind in {"access", "episode"} and evidence is None:
                return False
            if evidence is not None:
                if kind == "episode":
                    valid_evidence = self._validate_failure_evidence(
                        evidence, alias=alias, item_id=item_id, attempt=attempt,
                        error_code=payload["error_code"],
                        error_message=payload["error_message"],
                    )
                elif kind == "access":
                    valid_evidence = self._validate_access_failure_evidence(
                        evidence, alias=alias, attempt=attempt,
                        error_code=payload["error_code"],
                        error_message=payload["error_message"],
                    )
                else:
                    valid_evidence = False
                if not valid_evidence:
                    return False
            for flag in (
                "authorizes_private_execution", "authorizes_calibration",
                "authorizes_freeze",
            ):
                if payload.get(flag) is not False:
                    return False
            contracts.assert_artifact_safe(payload)
            return True
        except Exception:
            return False

    def _access_failure_evidence(self, *, phase: str, request: dict,
                                 error: Exception, catalog_raw=None,
                                 catalog_attestation=None,
                                 raw_call=None) -> dict:
        if phase not in {"catalog", "transport", "attestation"}:
            raise ValueError("access failure phase differs")
        evidence = {
            "failure_evidence_version": "crossroads-access-failure-v1",
            "failure_phase": phase,
            "request": deepcopy(request),
            "request_sha256": contracts.sha256_value(request),
            "catalog_raw": deepcopy(catalog_raw),
            "catalog_attestation": deepcopy(catalog_attestation),
            "raw_call": deepcopy(raw_call),
            "validation_error": {
                "code": type(error).__name__,
                "message": _safe_error_message(error),
            },
        }
        contracts.assert_artifact_safe(evidence)
        return evidence

    def _validate_access_failure_evidence(self, evidence: dict, *, alias: str,
                                          attempt: int, error_code: str,
                                          error_message: str) -> bool:
        try:
            expected_fields = {
                "failure_evidence_version", "failure_phase", "request",
                "request_sha256", "catalog_raw", "catalog_attestation",
                "raw_call", "validation_error",
            }
            if not isinstance(evidence, dict) or set(evidence) != expected_fields or (
                    evidence.get("failure_evidence_version")
                    != "crossroads-access-failure-v1"):
                return False
            model = contracts.resolve_model(alias)
            request = self._access_request(model, attempt)
            if evidence["request"] != request or evidence[
                    "request_sha256"] != contracts.sha256_value(request) or evidence[
                        "validation_error"] != {
                            "code": error_code, "message": error_message}:
                return False
            phase = evidence["failure_phase"]
            catalog_raw = evidence["catalog_raw"]
            catalog_attestation = evidence["catalog_attestation"]
            raw_call = evidence["raw_call"]
            if phase == "catalog":
                if catalog_raw is not None or catalog_attestation is not None or (
                        raw_call is not None):
                    return False
            elif phase in {"transport", "attestation"}:
                if contracts.validate_catalog(catalog_raw, model) != (
                        catalog_attestation):
                    return False
                if phase == "transport":
                    if raw_call is not None:
                        return False
                else:
                    if not isinstance(raw_call, dict):
                        return False
                    try:
                        executor.attest_call(raw_call, model)
                    except Exception as error:
                        if evidence["validation_error"] != {
                                "code": type(error).__name__,
                                "message": _safe_error_message(error)}:
                            return False
                    else:
                        return False
            else:
                return False
            contracts.assert_artifact_safe(evidence)
            return True
        except Exception:
            return False

    def _validate_failure_evidence(self, evidence: dict, *, alias: str,
                                   item_id: str, attempt: int,
                                   error_code: str, error_message: str) -> bool:
        try:
            model = contracts.resolve_model(alias)
            binding = self._request_binding(item_id)
            if executor.verify_episode_failure_evidence(
                    self.bank["episodes"][item_id], self.bank["truth"][item_id],
                    model=model, binding=binding, attempt=attempt,
                    evidence=evidence) is not True:
                return False
            if evidence["validation_error"] != {
                    "code": error_code, "message": error_message}:
                return False
            return True
        except Exception:
            return False

    def _validate_attempt_identity(self, payload: dict, *, kind: str,
                                   alias: str, item_id: str | None,
                                   attempt: int) -> bool:
        return (
            isinstance(payload, dict)
            and payload.get("kind") == kind
            and payload.get("model_alias") == alias
            and payload.get("item_id") == item_id
            and payload.get("attempt") == attempt
        )

    def _read_attempts(self, prefix: str, *, event: str, validator,
                       kind: str, alias: str,
                       item_id: str | None) -> list[dict]:
        referenced = {row["artifact"] for row in self.store.read_journal()}
        rows = []
        for attempt in range(1, 4):
            relative = f"{prefix}/attempt-{attempt}.json"
            path = self.root / relative
            if not path.exists():
                break
            validate_expected = lambda value, attempt=attempt: (
                self._validate_attempt_identity(
                    value, kind=kind, alias=alias, item_id=item_id,
                    attempt=attempt,
                )
                and validator(value) is True
            )
            if relative not in referenced:
                self.store.adopt_orphan(
                    relative, event=event, validator=validate_expected
                )
                referenced.add(relative)
            payload = _load_json(path)
            if validate_expected(payload) is not True:
                raise ValueError(f"existing attempt failed semantic replay: {relative}")
            rows.append(payload)
        return rows

    def _attempt_group(self, *, prefix: str, event: str, validator, operation,
                       kind: str, alias: str, item_id: str | None = None,
                       retry_failed: bool = False) -> dict:
        attempts = self._read_attempts(
            prefix, event=event, validator=validator, kind=kind,
            alias=alias, item_id=item_id,
        )
        for row in attempts:
            if row.get("status") == "success":
                return row
        if attempts and not retry_failed:
            raise ValueError(f"durable {kind} failure requires an explicit retry")
        next_attempt = len(attempts) + 1
        if next_attempt > 3:
            raise ValueError(f"{kind} exceeded the three-attempt ceiling")
        relative = f"{prefix}/attempt-{next_attempt}.json"
        binding = self._attempt_binding(
            kind=kind, alias=alias, item_id=item_id, attempt=next_attempt
        )
        try:
            payload = operation(next_attempt)
        except Exception as error:
            payload = self._safe_failure(
                kind=kind, alias=alias, attempt=next_attempt,
                item_id=item_id, binding=binding, error=error,
            )
        if payload.get("status") == "failed" and payload.get(
                "failure_evidence") is None:
            raise RuntimeError(
                f"{kind} failed before bound failure evidence; attempt not committed"
            )
        self.store.commit(relative, payload, event=event)
        if not self._validate_attempt_identity(
                payload, kind=kind, alias=alias, item_id=item_id,
                attempt=next_attempt) or validator(payload) is not True:
            raise ValueError("new attempt failed semantic validation")
        if payload["status"] == "success":
            return payload
        raise RuntimeError(
            f"{kind} failed attempt {next_attempt}; rerun with explicit retry"
        )

    def _access_request(self, model: dict, attempt: int) -> dict:
        body = {
            "model": model["alias"],
            "messages": [
                {"role": "system", "content": "Return a JSON object acknowledging access."},
                {"role": "user", "content": "Return {\"access\":true}."},
            ],
            "max_completion_tokens": 512,
            "reasoning": {"effort": model["reasoning_effort"]},
            "response_format": {"type": "json_object"},
            "usage": {"include": True},
            "provider": deepcopy(model["routing"]),
        }
        request = {
            "request_version": "crossroads-access-probe-v3",
            "purpose": "public qualification", "measurement_ready": False,
            "model_alias": model["alias"],
            "expected_snapshot": model["expected_snapshot"],
            "attempt": attempt,
            "binding": {
                "bank_sha256": self.manifest["hashes"]["bank"],
                "profile_sha256": self.manifest["hashes"]["profile"],
            },
            "transport_body": body,
        }
        contracts.assert_artifact_safe(request)
        return request

    def _access_success(self, alias: str, attempt: int) -> dict:
        model = contracts.resolve_model(alias)
        request = self._access_request(model, attempt)
        try:
            catalog_raw = self.client.catalog(alias)
            catalog_attestation = contracts.validate_catalog(catalog_raw, model)
        except Exception as error:
            raise _AccessFailureError(
                error, self._access_failure_evidence(
                    phase="catalog", request=request, error=error,
                )
            ) from None
        try:
            raw_call = self.client.complete(deepcopy(request["transport_body"]))
        except Exception as error:
            raise _AccessFailureError(
                error, self._access_failure_evidence(
                    phase="transport", request=request, error=error,
                    catalog_raw=catalog_raw,
                    catalog_attestation=catalog_attestation,
                )
            ) from None
        try:
            call_attestation = executor.attest_call(raw_call, model)
        except Exception as error:
            raise _AccessFailureError(
                error, self._access_failure_evidence(
                    phase="attestation", request=request, error=error,
                    catalog_raw=catalog_raw,
                    catalog_attestation=catalog_attestation,
                    raw_call=raw_call,
                )
            ) from None
        return {
            "artifact_version": "crossroads-qualification-attempt-v2",
            "kind": "access", "status": "success",
            "purpose": "public qualification",
            "provenance": self.manifest["provenance"],
            "measurement_ready": False, "public_qualification_evidence": True,
            "model_alias": alias, "item_id": None, "attempt": attempt,
            "request": request, "request_sha256": contracts.sha256_value(request),
            "catalog_raw": catalog_raw, "catalog_attestation": catalog_attestation,
            "raw_call": raw_call, "call_attestation": call_attestation,
            "authorizes_private_execution": False,
            "authorizes_calibration": False, "authorizes_freeze": False,
        }

    def _validate_access(self, payload: dict) -> bool:
        if not isinstance(payload, dict) or payload.get("kind") != "access":
            return False
        if payload.get("status") == "failed":
            return self._validate_failure(
                payload, kind="access", alias=payload.get("model_alias"),
                item_id=None, attempt=payload.get("attempt"),
            )
        if payload.get("status") != "success":
            return False
        alias = payload.get("model_alias")
        try:
            model = contracts.resolve_model(alias)
            if (
                payload.get("artifact_version")
                != "crossroads-qualification-attempt-v2"
                or payload.get("purpose") != "public qualification"
                or payload.get("provenance") != self.manifest["provenance"]
                or payload.get("measurement_ready") is not False
                or payload.get("public_qualification_evidence") is not True
                or payload.get("item_id") is not None
                or type(payload.get("attempt")) is not int
                or not 1 <= payload["attempt"] <= 3
                or any(payload.get(flag) is not False for flag in (
                    "authorizes_private_execution", "authorizes_calibration",
                    "authorizes_freeze",
                ))
            ):
                return False
            if contracts.validate_catalog(payload["catalog_raw"], model) != payload[
                    "catalog_attestation"]:
                return False
            if executor.attest_call(payload["raw_call"], model) != payload[
                    "call_attestation"]:
                return False
            request = self._access_request(model, payload["attempt"])
            return (
                payload["request"] == request
                and payload["request_sha256"] == contracts.sha256_value(request)
                and payload.get("measurement_ready") is False
            )
        except (KeyError, ValueError, TypeError):
            return False

    def access(self, *, retry_failed: bool = False) -> list[dict]:
        if self._phase_complete("access"):
            return self._successful("access")
        rows = []
        for alias in self.manifest["models"]:
            prefix = f"access/{_slug(alias)}"
            rows.append(self._attempt_group(
                prefix=prefix, event="access_attempt", validator=self._validate_access,
                operation=lambda attempt, alias=alias: self._access_success(alias, attempt),
                kind="access", alias=alias, retry_failed=retry_failed,
            ))
        self.store.complete_phase("access")
        return rows

    def _episode_success(self, alias: str, item_id: str, attempt: int,
                         *, fork_only: bool) -> dict:
        episode = self.bank["episodes"][item_id]
        truth = self.bank["truth"][item_id]
        model = contracts.resolve_model(alias)
        binding = self._request_binding(item_id)
        result = executor.run_episode(
            episode, truth, model=model, client=self.client, binding=binding,
            attempt=attempt, provenance=self.manifest["provenance"],
            fork_only=fork_only,
        )
        return {
            "artifact_version": "crossroads-qualification-attempt-v2",
            "kind": "episode", "status": "success",
            "purpose": "public qualification",
            "provenance": self.manifest["provenance"],
            "measurement_ready": False, "public_qualification_evidence": True,
            "model_alias": alias, "item_id": item_id, "attempt": attempt,
            "binding": binding, "result": result,
            "authorizes_private_execution": False,
            "authorizes_calibration": False, "authorizes_freeze": False,
        }

    def _validate_episode(self, payload: dict) -> bool:
        if not isinstance(payload, dict) or payload.get("kind") != "episode":
            return False
        if payload.get("status") == "failed":
            return self._validate_failure(
                payload, kind="episode", alias=payload.get("model_alias"),
                item_id=payload.get("item_id"), attempt=payload.get("attempt"),
            )
        if payload.get("status") != "success":
            return False
        alias, item_id = payload.get("model_alias"), payload.get("item_id")
        if alias not in self.manifest["models"] or item_id not in self.bank["episodes"]:
            return False
        if (
            payload.get("artifact_version")
            != "crossroads-qualification-attempt-v2"
            or payload.get("purpose") != "public qualification"
            or payload.get("provenance") != self.manifest["provenance"]
            or payload.get("measurement_ready") is not False
            or payload.get("public_qualification_evidence") is not True
            or type(payload.get("attempt")) is not int
            or not 1 <= payload["attempt"] <= 3
            or any(payload.get(flag) is not False for flag in (
                "authorizes_private_execution", "authorizes_calibration",
                "authorizes_freeze",
            ))
        ):
            return False
        binding = self._request_binding(item_id)
        if payload.get("binding") != binding:
            return False
        try:
            return payload.get("result", {}).get("attempt") == payload[
                "attempt"] and executor.verify_episode_result(
                self.bank["episodes"][item_id], self.bank["truth"][item_id],
                model=contracts.resolve_model(alias), result=payload["result"],
                binding=binding,
            )
        except (KeyError, ValueError, TypeError):
            return False

    def _run_items(self, item_ids: list[str], *, fork_only: bool,
                   retry_failed: bool = False) -> list[dict]:
        rows = []
        for alias in self.manifest["models"]:
            for item_id in item_ids:
                prefix = f"episodes/{_slug(alias)}/{item_id}"
                rows.append(self._attempt_group(
                    prefix=prefix, event="episode_attempt",
                    validator=self._validate_episode,
                    operation=lambda attempt, alias=alias, item_id=item_id: self._episode_success(
                        alias, item_id, attempt, fork_only=fork_only
                    ),
                    kind="episode", alias=alias, item_id=item_id,
                    retry_failed=retry_failed,
                ))
        return rows

    def canary(self, *, retry_failed: bool = False) -> list[dict]:
        if self.manifest["execution_mode"] != executor.STAGED_MODE:
            raise ValueError("canary requires path-only staged qualification")
        if not self._phase_complete("access"):
            raise ValueError("access phase must complete before canary")
        if self._phase_complete("canary"):
            return self._successful("episode", self.manifest["canary_item_ids"])
        rows = self._run_items(
            self.manifest["canary_item_ids"], fork_only=False,
            retry_failed=retry_failed,
        )
        self.store.complete_phase("canary")
        return rows

    def _successful(self, kind: str, item_ids: list[str] | None = None) -> list[dict]:
        rows = []
        for entry in self.store.read_journal():
            relative = entry["artifact"]
            if relative is None or not relative.endswith(".json"):
                continue
            payload = _load_json(self.root / relative)
            if payload.get("kind") == kind and payload.get("status") == "success":
                if item_ids is None or payload.get("item_id") in item_ids:
                    rows.append(payload)
        return sorted(rows, key=lambda row: (
            row.get("model_alias", ""), row.get("item_id") or ""
        ))

    def _commit_report(self, filename: str, report: dict) -> dict:
        path = self.root / filename
        referenced = {row["artifact"] for row in self.store.read_journal()}
        if path.exists() and filename not in referenced:
            self.store.adopt_orphan(
                filename, event="report_frozen", validator=lambda value: value == report
            )
        elif not path.exists():
            self.store.commit(filename, report, event="report_frozen")
        elif _load_json(path) != report:
            raise ValueError("immutable report differs from semantic replay")
        return report

    def smoke(self, *, retry_failed: bool = False) -> dict:
        if self.manifest["execution_mode"] != executor.STAGED_MODE:
            raise ValueError("smoke requires path-only staged qualification")
        if self._phase_complete("report"):
            return self.load_report()
        if not self._phase_complete("canary"):
            raise ValueError("canary phase must complete before smoke")
        if not self._phase_complete("smoke"):
            self._run_items(
                self.manifest["public_item_ids"], fork_only=False,
                retry_failed=retry_failed,
            )
            self.store.complete_phase("smoke")
        artifacts = self._successful("episode", self.manifest["public_item_ids"])
        report = build_report(
            manifest=self.manifest, successful_artifacts=artifacts,
            episodes=self.bank["episodes"], truth=self.bank["truth"],
        )
        self._commit_report("qualification_report.json", report)
        if not self._phase_complete("report"):
            self.store.complete_phase("report")
        return report

    def diagnose(self, *, retry_failed: bool = False) -> dict:
        if self.manifest["execution_mode"] != executor.DIAGNOSTIC_MODE:
            raise ValueError("diagnose requires fork-only diagnostic manifest")
        if self._phase_complete("report"):
            return self.load_report(diagnostic=True)
        if not self._phase_complete("access"):
            raise ValueError("access phase must complete before diagnostic")
        if not self._phase_complete("diagnostic"):
            self._run_items(
                self.manifest["public_item_ids"], fork_only=True,
                retry_failed=retry_failed,
            )
            self.store.complete_phase("diagnostic")
        artifacts = self._successful("episode", self.manifest["public_item_ids"])
        report = build_report(
            manifest=self.manifest, successful_artifacts=artifacts,
            episodes=self.bank["episodes"], truth=self.bank["truth"],
            diagnostic=True,
        )
        self._commit_report("diagnostic_report.json", report)
        if not self._phase_complete("report"):
            self.store.complete_phase("report")
        return report

    def load_report(self, diagnostic: bool = False) -> dict:
        filename = "diagnostic_report.json" if diagnostic else "qualification_report.json"
        return _load_json(self.root / filename)
