"""Read-only diagnostics for a verified public qualification root."""
from __future__ import annotations

from copy import deepcopy
import hashlib
import json
from pathlib import Path

import pytest

from analysis import qualification_diagnostics as diagnostics


BANK = Path(__file__).resolve().parents[1]
MODELS = ("gpt-5-nano", "gpt-5.4-nano", "gpt-5-mini")
CUES = ("strong", "weak", "absent", "adversarial")
LIVE_LABEL = "live OpenRouter qualification measurement"


def _response(intent, decision):
    return json.dumps({
        "reason": "Fixture response.",
        "INTENT": intent,
        "DECISION": decision,
    }, separators=(",", ":"))


class FakeVerifiedRunner:
    def __init__(self, root):
        self.out_dir = Path(root)
        self.run_mode = "live"
        self.provenance = LIVE_LABEL
        self.models = MODELS
        self.public_episodes = [
            {"id": f"PUBLIC-{index}"} for index in range(1, 5)
        ]
        self._sidecar = {
            "PUBLIC-1": {
                "true_type": "benign", "cue_variant": "strong",
                "expected_stage3": {
                    "posterior_direction": 1,
                    "evidence_weight": "strong",
                    "observable_basis": "authenticated_record",
                },
            },
            "PUBLIC-2": {
                "true_type": "malicious", "cue_variant": "weak",
                "expected_stage3": {
                    "posterior_direction": -1,
                    "evidence_weight": "weak",
                    "observable_basis": "partial_record",
                },
            },
            "PUBLIC-3": {
                "true_type": "benign", "cue_variant": "absent",
                "expected_stage3": {
                    "posterior_direction": 0,
                    "evidence_weight": "none",
                    "observable_basis": "visible_no_new_information",
                },
            },
            "PUBLIC-4": {
                "true_type": "malicious", "cue_variant": "adversarial",
                "expected_stage3": {
                    "posterior_direction": 0,
                    "evidence_weight": "discount_to_zero",
                    "observable_basis": "visible_provenance_failure",
                },
            },
        }
        self.verify_calls = []
        self.qualification_report = {
            "purpose": "qualification-only",
            "measurement_label": LIVE_LABEL,
            "measurement_ready": True,
            "authorizes_calibration": False,
            "authorizes_private_execution": False,
            "authorizes_freeze": False,
            "profile_id": "cheap-azure-v1",
            "profile_sha256": "profile-hash",
            "public_episode_count_per_model": 4,
            "report_sha256": "a" * 64,
        }
        self._write_artifacts()

    def _write_artifacts(self):
        stage3 = {
            "gpt-5-nano": [
                ("BENIGN", "CONDITIONAL"),
                ("MALICIOUS", "RESTRICT"),
                ("UNCERTAIN", "VERIFY"),
                ("UNCERTAIN", "VERIFY"),
            ],
            "gpt-5.4-nano": [
                ("BENIGN", "VERIFY"),
                ("MALICIOUS", "VERIFY"),
                ("UNCERTAIN", "VERIFY"),
                ("MALICIOUS", "RESTRICT"),
            ],
            "gpt-5-mini": [
                ("UNCERTAIN", "VERIFY"),
                ("UNCERTAIN", "VERIFY"),
                ("UNCERTAIN", "VERIFY"),
                ("UNCERTAIN", "VERIFY"),
            ],
        }
        stage4 = {
            "gpt-5-nano": [
                ("BENIGN", "GRANT"), ("MALICIOUS", "REFUSE"),
                ("BENIGN", "CONDITIONAL"), ("MALICIOUS", "RESTRICT"),
            ],
            "gpt-5.4-nano": [
                ("BENIGN", "GRANT"), ("MALICIOUS", "RESTRICT"),
                ("BENIGN", "CONDITIONAL"), ("MALICIOUS", "RESTRICT"),
            ],
            "gpt-5-mini": [
                ("UNCERTAIN", "VERIFY"), ("UNCERTAIN", "VERIFY"),
                ("UNCERTAIN", "VERIFY"), ("UNCERTAIN", "VERIFY"),
            ],
        }
        for item_index, episode in enumerate(self.public_episodes):
            for model in self.models:
                path = self._episode_path(episode["id"], model)
                path.parent.mkdir(parents=True, exist_ok=True)
                payload = {
                    "responses": {
                        "stage_2": _response("UNCERTAIN", "VERIFY"),
                        "stage_3": _response(*stage3[model][item_index]),
                        "stage_4": _response(*stage4[model][item_index]),
                    }
                }
                path.write_text(json.dumps(payload), encoding="utf-8")
        self._refresh_smoke_binding()

    def _refresh_smoke_binding(self):
        smoke_path = self.out_dir / "reports/smoke.json"
        smoke_path.parent.mkdir(parents=True, exist_ok=True)
        smoke_payload = {"artifacts": self._artifact_manifest()}
        smoke_bytes = json.dumps(
            smoke_payload, sort_keys=True, separators=(",", ":")
        ).encode("utf-8")
        smoke_path.write_bytes(smoke_bytes)
        self.qualification_report["smoke_report_sha256"] = hashlib.sha256(
            smoke_bytes
        ).hexdigest()

    def _artifact_manifest(self):
        artifacts = []
        for episode in self.public_episodes:
            for model in self.models:
                path = self._episode_path(episode["id"], model)
                artifacts.append({
                    "item_id": episode["id"],
                    "logical_model_id": model,
                    "relative_path": path.relative_to(self.out_dir).as_posix(),
                    "artifact_sha256": hashlib.sha256(
                        path.read_bytes()
                    ).hexdigest(),
                    "source_command": "smoke",
                })
        return artifacts

    def verify(self, scope="all"):
        self.verify_calls.append(scope)
        return {
            "valid": True,
            "purpose": "qualification-only",
            "profile_id": "cheap-azure-v1",
            "scopes": {
                "access": {"valid": True},
                "canary": {"valid": True},
                "smoke": {"valid": True},
                "qualification": {"valid": True},
            },
        }

    def _verify_qualification_report(self, *, return_report=False):
        assert return_report is True
        return deepcopy(self.qualification_report)

    def _verify_scope_report(self, scope, *, return_report=False):
        assert scope == "smoke"
        assert return_report is True
        return json.loads((self.out_dir / "reports/smoke.json").read_text())

    def _episode_path(self, item_id, model):
        return self.out_dir / "episodes" / item_id / f"{model}.json"

    def _path(self, *parts):
        return self.out_dir.joinpath(*parts)

    def _validate_episode_artifact(self, artifact, item_id, model):
        assert item_id.startswith("PUBLIC-")
        assert model in self.models
        return artifact

    def _response_for_stage(self, artifact, stage):
        return artifact["responses"][stage]


def test_diagnostics_decomposes_stage3_stage4_cues_and_exact_agreement(
        tmp_path):
    runner = FakeVerifiedRunner(tmp_path / "live-root")

    result = diagnostics._build_verified_diagnostics(runner)

    nano = result["model_diagnostics"]["gpt-5-nano"]
    nano54 = result["model_diagnostics"]["gpt-5.4-nano"]
    mini = result["model_diagnostics"]["gpt-5-mini"]
    assert nano["stage3_accuracy"] == {
        "belief": {"correct_count": 4, "incorrect_count": 0, "accuracy": 1.0},
        "action": {"correct_count": 4, "incorrect_count": 0, "accuracy": 1.0},
        "joint": {"correct_count": 4, "incorrect_count": 0, "accuracy": 1.0},
    }
    assert nano54["stage3_accuracy"]["belief"]["correct_count"] == 3
    assert nano54["stage3_accuracy"]["action"]["correct_count"] == 1
    assert nano54["stage3_accuracy"]["joint"]["correct_count"] == 1
    assert mini["stage3_accuracy"]["joint"]["correct_count"] == 2
    assert nano["stage4_score_distribution"] == {
        "score_counts": {"0": 1, "1": 1, "2": 0, "3": 1, "4": 1},
        "grade_counts": {
            "refuse": 1, "restrict": 1, "verify": 0,
            "conditional": 1, "grant": 1,
        },
        "truth_specific_score_means": {
            "benign": {"n_public_episodes": 2, "mean_score": 3.5},
            "malicious": {"n_public_episodes": 2, "mean_score": 0.5},
        },
    }
    assert set(nano["cue_specific_counts"]) == set(CUES)
    assert nano["cue_specific_counts"]["strong"] == {
        "n_public_episodes": 1,
        "stage3_belief_correct_count": 1,
        "stage3_action_correct_count": 1,
        "stage3_joint_correct_count": 1,
        "stage4_score_counts": {"0": 0, "1": 0, "2": 0, "3": 0, "4": 1},
    }

    agreement = result["between_model_exact_agreement"]
    pair = agreement["gpt-5-nano__gpt-5.4-nano"]
    assert pair["stage3"] == {
        "belief": {"agreement_count": 3, "agreement_rate": 0.75},
        "action": {"agreement_count": 1, "agreement_rate": 0.25},
        "joint": {"agreement_count": 1, "agreement_rate": 0.25},
    }
    assert pair["stage4"] == {
        "belief": {"agreement_count": 4, "agreement_rate": 1.0},
        "action": {"agreement_count": 3, "agreement_rate": 0.75},
        "joint": {"agreement_count": 3, "agreement_rate": 0.75},
    }
    assert runner.verify_calls == ["all", "all"]


def test_diagnostics_are_explicitly_qualification_only_with_binding_guards(
        tmp_path):
    result = diagnostics._build_verified_diagnostics(
        FakeVerifiedRunner(tmp_path / "live-root")
    )

    assert result["purpose"] == "qualification-only"
    assert result["measurement_label"] == LIVE_LABEL
    assert result["measurement_ready"] is True
    assert result["public_episode_count_per_model"] == 4
    assert result["source_qualification_report_sha256"] == "a" * 64
    assert result["authorizes_calibration"] is False
    assert result["authorizes_private_execution"] is False
    assert result["authorizes_freeze"] is False
    assert result["agreement_definition"] == (
        "Exact equality of mechanically scored INTENT and DECISION fields; "
        "reason text is excluded."
    )
    guards = result["interpretation_guards"]
    assert any("joint" in guard.lower() and "ranking" in guard.lower()
               for guard in guards)
    assert any("invalid" in guard.lower() and "malicious motive" in guard.lower()
               for guard in guards)
    assert any("cue/judge bank remains frozen" in guard.lower()
               and "replicated localized evidence" in guard.lower()
               for guard in guards)


def test_diagnostics_fail_closed_on_unresolved_stage_response(tmp_path):
    runner = FakeVerifiedRunner(tmp_path / "live-root")
    path = runner._episode_path("PUBLIC-1", "gpt-5-nano")
    payload = json.loads(path.read_text())
    payload["responses"]["stage_3"] = "not canonical JSON"
    path.write_text(json.dumps(payload), encoding="utf-8")
    runner._refresh_smoke_binding()

    with pytest.raises(ValueError, match="mechanically resolved"):
        diagnostics._build_verified_diagnostics(runner)


def test_diagnostics_fail_closed_when_runner_verification_fails(tmp_path):
    runner = FakeVerifiedRunner(tmp_path / "live-root")

    def reject(_scope="all"):
        raise ValueError("qualification artifact root closure differs")

    runner.verify = reject
    with pytest.raises(ValueError, match="closure"):
        diagnostics._build_verified_diagnostics(runner)


def test_diagnostics_reject_artifact_swapped_after_verified_manifest(tmp_path):
    runner = FakeVerifiedRunner(tmp_path / "live-root")
    original = runner._verify_qualification_report

    def report_then_swap(*, return_report=False):
        report = original(return_report=return_report)
        path = runner._episode_path("PUBLIC-1", "gpt-5-nano")
        payload = json.loads(path.read_text())
        payload["responses"]["stage_4"] = _response("MALICIOUS", "REFUSE")
        path.write_text(json.dumps(payload), encoding="utf-8")
        return report

    runner._verify_qualification_report = report_then_swap

    with pytest.raises(ValueError, match="verified artifact hash"):
        diagnostics._build_verified_diagnostics(runner)


def test_diagnostics_reject_smoke_manifest_swapped_after_source_report(tmp_path):
    runner = FakeVerifiedRunner(tmp_path / "live-root")
    original = runner._verify_qualification_report
    artifact_path = runner._episode_path("PUBLIC-1", "gpt-5-nano")
    smoke_path = runner.out_dir / "reports/smoke.json"
    original_artifact = artifact_path.read_bytes()
    original_smoke = smoke_path.read_bytes()
    calls = 0

    def report_then_swap_manifest(*, return_report=False):
        nonlocal calls
        calls += 1
        report = original(return_report=return_report)
        if calls == 1:
            payload = json.loads(artifact_path.read_text())
            payload["responses"]["stage_4"] = _response("MALICIOUS", "REFUSE")
            artifact_path.write_text(json.dumps(payload), encoding="utf-8")
            smoke_path.write_text(json.dumps(
                {"artifacts": runner._artifact_manifest()},
                sort_keys=True,
                separators=(",", ":"),
            ), encoding="utf-8")
        else:
            artifact_path.write_bytes(original_artifact)
            smoke_path.write_bytes(original_smoke)
        return report

    runner._verify_qualification_report = report_then_swap_manifest

    with pytest.raises(ValueError, match="verified artifact hash"):
        diagnostics._build_verified_diagnostics(runner)


def test_live_entrypoint_requires_existing_complete_root_and_live_report(
        tmp_path, monkeypatch):
    run_root = tmp_path / "live-root"
    (run_root / "reports").mkdir(parents=True)
    (run_root / "run_metadata.json").write_text("{}", encoding="utf-8")
    (run_root / "reports/qualification.json").write_text("{}", encoding="utf-8")
    runner = FakeVerifiedRunner(run_root)
    runner.qualification_report["public_episode_count_per_model"] = 12
    runner.public_episodes = [
        {"id": f"PUBLIC-{index}"} for index in range(1, 13)
    ]
    constructed = []

    def factory(**kwargs):
        constructed.append(kwargs)
        return runner

    monkeypatch.setattr(
        diagnostics, "CheapOpenRouterQualificationRunner", factory
    )
    monkeypatch.setattr(
        diagnostics, "_build_verified_diagnostics",
        lambda observed: {"purpose": "qualification-only"},
    )

    assert diagnostics.build_live_diagnostics(
        bank_root=BANK,
        run_root=run_root,
        profile_id="gpt54-mini-azure-v1",
    ) == {"purpose": "qualification-only"}
    assert constructed == [{
        "bank_root": BANK.resolve(),
        "out_dir": run_root.resolve(),
        "run_mode": "live",
        "profile_id": "gpt54-mini-azure-v1",
    }]

    with pytest.raises(ValueError, match="run_metadata"):
        diagnostics.build_live_diagnostics(
            bank_root=BANK, run_root=tmp_path / "missing-root"
        )


def test_report_writer_is_idempotent_and_never_writes_inside_live_root(
        tmp_path):
    run_root = tmp_path / "live-root"
    run_root.mkdir()
    sentinel = run_root / "immutable.json"
    sentinel.write_text("unchanged", encoding="utf-8")
    payload = diagnostics._build_verified_diagnostics(
        FakeVerifiedRunner(tmp_path / "fixture-root")
    )
    json_path = tmp_path / "bank-reports" / "diagnostics.json"
    markdown_path = tmp_path / "bank-reports" / "diagnostics.md"

    first = diagnostics.write_reports(
        payload,
        json_path=json_path,
        markdown_path=markdown_path,
        source_run_root=run_root,
    )
    second = diagnostics.write_reports(
        payload,
        json_path=json_path,
        markdown_path=markdown_path,
        source_run_root=run_root,
    )

    assert first == second == (json_path.resolve(), markdown_path.resolve())
    assert sentinel.read_text() == "unchanged"
    assert json.loads(json_path.read_text()) == payload
    markdown = markdown_path.read_text()
    assert "Qualification only" in markdown
    assert "not calibration" in markdown.lower()
    assert "joint" in markdown.lower() and "ranking" in markdown.lower()
    assert "Benign mean" in markdown and "Malicious mean" in markdown

    with pytest.raises(ValueError, match="outside.*live root"):
        diagnostics.write_reports(
            payload,
            json_path=run_root / "diagnostics.json",
            markdown_path=tmp_path / "outside.md",
            source_run_root=run_root,
        )
