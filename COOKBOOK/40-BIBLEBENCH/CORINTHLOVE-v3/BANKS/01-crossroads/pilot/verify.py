"""Whole-root and semantic replay verification for public qualification runs."""
from __future__ import annotations

import json
from pathlib import Path, PurePosixPath

from . import contracts
from .evidence import verify_evidence_root
from .report import build_report
from .runner import QualificationRunner, _slug


_PHASES = {
    "path-only staged qualification": ("access", "canary", "smoke", "report"),
    "fork-only diagnostic": ("access", "diagnostic", "report"),
}


class _NoNetworkClient:
    """Verifier placeholder: semantic replay never invokes a provider."""

    def catalog(self, _alias):  # pragma: no cover - defensive tripwire
        raise RuntimeError("verification cannot access the network")

    def complete(self, _body):  # pragma: no cover - defensive tripwire
        raise RuntimeError("verification cannot access the network")


def _read(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def _common_attempt(payload: dict, manifest: dict) -> None:
    if not isinstance(payload, dict):
        raise ValueError("qualification attempt is not an object")
    if payload.get("artifact_version") != "crossroads-qualification-attempt-v2":
        raise ValueError("qualification attempt version differs")
    if payload.get("purpose") != "public qualification" or payload.get(
            "provenance") != manifest["provenance"]:
        raise ValueError("qualification attempt purpose/provenance differs")
    if payload.get("measurement_ready") is not False or payload.get(
            "public_qualification_evidence") is not True:
        raise ValueError("qualification attempt measurement label differs")
    if payload.get("model_alias") not in manifest["models"]:
        raise ValueError("qualification attempt model is outside the manifest")
    if type(payload.get("attempt")) is not int or not 1 <= payload["attempt"] <= 3:
        raise ValueError("qualification attempt ordinal is invalid")
    if payload.get("status") not in {"success", "failed"}:
        raise ValueError("qualification attempt status is invalid")
    for flag in (
        "authorizes_private_execution", "authorizes_calibration",
        "authorizes_freeze",
    ):
        if payload.get(flag) is not False:
            raise ValueError("qualification attempt authorization differs")
    contracts.assert_artifact_safe(payload)


def _expected_pairs(models: list[str], item_ids: list[str]) -> set[tuple[str, str]]:
    return {(model, item_id) for model in models for item_id in item_ids}


def verify_run(root: Path, *, bank_root: Path,
               require_phase: str | None = None) -> dict:
    """Replay a qualification root without a provider or credential.

    Verification first closes the byte-level journal, then rebinds the current
    public bank/profile/scorers and rebuilds every access attestation, episode
    request, tool effect, classification, and report.
    """
    root = Path(root).expanduser().absolute()
    closure = verify_evidence_root(root)
    runner = QualificationRunner.open(
        root, bank_root=bank_root, client=_NoNetworkClient()
    )
    manifest = runner.manifest
    mode = manifest.get("execution_mode")
    if mode not in _PHASES:
        raise ValueError("qualification execution mode differs")
    allowed_phases = _PHASES[mode]
    if require_phase is not None and require_phase not in allowed_phases:
        raise ValueError("required phase is incompatible with execution mode")

    journal = runner.store.read_journal()
    completed = [
        row["event"].split(":", 1)[1] for row in journal
        if row["event"].startswith("phase_complete:")
    ]
    if completed != list(allowed_phases[:len(completed)]):
        raise ValueError("qualification phases are incomplete or out of order")
    if require_phase is not None and require_phase not in completed:
        raise ValueError(f"required phase is incomplete: {require_phase}")

    access_success: set[str] = set()
    episode_success: set[tuple[str, str]] = set()
    reports: dict[str, dict] = {}
    attempt_artifacts = 0
    for entry in journal:
        relative = entry["artifact"]
        if relative is None or relative in {"manifest.json", "canary_selection.json"}:
            continue
        payload = _read(root / relative)
        parts = PurePosixPath(relative).parts
        if parts[0] == "access":
            if entry["event"] != "access_attempt" or len(parts) != 3:
                raise ValueError("access artifact path/event differs")
            _common_attempt(payload, manifest)
            if payload.get("kind") != "access" or payload.get("item_id") is not None:
                raise ValueError("access artifact identity differs")
            expected = f"attempt-{payload['attempt']}.json"
            if parts[1] != _slug(payload["model_alias"]) or parts[2] != expected:
                raise ValueError("access artifact path binding differs")
            if runner._validate_access(payload) is not True:
                raise ValueError("access artifact failed semantic replay")
            if payload["status"] == "success":
                access_success.add(payload["model_alias"])
            attempt_artifacts += 1
        elif parts[0] == "episodes":
            if entry["event"] != "episode_attempt" or len(parts) != 4:
                raise ValueError("episode artifact path/event differs")
            _common_attempt(payload, manifest)
            item_id = payload.get("item_id")
            if payload.get("kind") != "episode" or item_id not in runner.bank["episodes"]:
                raise ValueError("episode artifact identity differs")
            expected = f"attempt-{payload['attempt']}.json"
            if parts[1] != _slug(payload["model_alias"]) or parts[2] != item_id or (
                    parts[3] != expected):
                raise ValueError("episode artifact path binding differs")
            if runner._validate_episode(payload) is not True:
                raise ValueError("episode artifact failed semantic replay")
            if payload["status"] == "success":
                episode_success.add((payload["model_alias"], item_id))
            attempt_artifacts += 1
        elif relative in {"qualification_report.json", "diagnostic_report.json"}:
            if entry["event"] != "report_frozen":
                raise ValueError("report artifact event differs")
            reports[relative] = payload
        else:
            raise ValueError(f"unknown qualification artifact: {relative}")

    models = manifest["models"]
    if "access" in completed and access_success != set(models):
        raise ValueError("completed access phase lacks one success per model")
    if "canary" in completed:
        expected = _expected_pairs(models, manifest["canary_item_ids"])
        if not expected <= episode_success:
            raise ValueError("completed canary phase lacks model/item coverage")
    terminal_items = manifest["public_item_ids"]
    terminal_phase = "diagnostic" if mode == "fork-only diagnostic" else "smoke"
    if terminal_phase in completed:
        expected = _expected_pairs(models, terminal_items)
        if episode_success != expected:
            raise ValueError("completed public phase has incomplete/extra coverage")

    report_name = (
        "diagnostic_report.json" if mode == "fork-only diagnostic"
        else "qualification_report.json"
    )
    if "report" in completed:
        if set(reports) != {report_name}:
            raise ValueError("completed report phase has missing/extra report")
        artifacts = runner._successful("episode", terminal_items)
        replay = build_report(
            manifest=manifest, successful_artifacts=artifacts,
            episodes=runner.bank["episodes"], truth=runner.bank["truth"],
            diagnostic=mode == "fork-only diagnostic",
        )
        if reports[report_name] != replay:
            raise ValueError("qualification report failed semantic replay")
    elif reports:
        raise ValueError("qualification report exists before report completion")

    return {
        "valid": True,
        "purpose": "public qualification",
        "provenance": manifest["provenance"],
        "measurement_ready": False,
        "execution_mode": mode,
        "canonical_e_measurement": False,
        "issues_live_judges": False,
        "authorizes_model_ranking": False,
        "models": list(models),
        "phases_complete": completed,
        "attempt_artifacts": attempt_artifacts,
        "successful_access_artifacts": len(access_success),
        "successful_episode_artifacts": len(episode_success),
        "journal_entries": closure["journal_entries"],
        "artifacts": closure["artifacts"],
        "authorizes_private_execution": False,
        "authorizes_calibration": False,
        "authorizes_freeze": False,
    }
