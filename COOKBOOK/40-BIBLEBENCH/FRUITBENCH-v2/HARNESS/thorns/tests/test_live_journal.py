from __future__ import annotations

from dataclasses import replace
import hashlib
import json
import os
from pathlib import Path
import sys

import pytest


HARNESS = Path(__file__).resolve().parents[1]
if str(HARNESS) not in sys.path:
    sys.path.insert(0, str(HARNESS))

import live_journal  # noqa: E402
from live_journal import (  # noqa: E402
    CompletedJournalError,
    IncompleteJournalError,
    JournalIntegrityError,
    LiveEvidenceJournal,
    PathReservationError,
    ResumeRefusedError,
    RunIdentity,
    SecretMaterialError,
    read_completed_journal,
    validate_journal,
)


def _identity(**overrides: str) -> RunIdentity:
    values = {
        "run_id": "thorns-live-unit-001",
        "config_sha256": "1" * 64,
        "source_sha256": "2" * 64,
        "schedule_sha256": "3" * 64,
        "receipt_sha256": "4" * 64,
    }
    values.update(overrides)
    return RunIdentity(**values)


def _paths(tmp_path: Path):
    return (
        tmp_path / "evidence.jsonl",
        [tmp_path / "raw.json", tmp_path / "aggregate.json"],
    )


def _decode_rows(path: Path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]


def _event_hash(row):
    material = {key: value for key, value in row.items() if key != "event_hash"}
    encoded = json.dumps(
        material,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def test_create_exclusively_reserves_every_path_and_writes_canonical_start(tmp_path):
    journal_path, outputs = _paths(tmp_path)

    journal = LiveEvidenceJournal.create(
        journal_path,
        output_paths=outputs,
        identity=_identity(),
        resumable=True,
    )
    journal.close()

    assert journal_path.is_file()
    assert [path.read_bytes() for path in outputs] == [b"", b""]
    assert journal_path.stat().st_mode & 0o777 == 0o600
    rows = _decode_rows(journal_path)
    assert len(rows) == 1
    assert rows[0]["event_type"] == "run_start"
    assert rows[0]["sequence"] == 0
    assert rows[0]["previous_hash"] == "0" * 64
    assert rows[0]["event_hash"] == _event_hash(rows[0])
    assert rows[0]["payload"]["identity"] == _identity().as_dict()
    assert rows[0]["payload"]["resumable"] is True
    assert {entry["path"] for entry in rows[0]["payload"]["reservations"]} == {
        str(journal_path.resolve()),
        *(str(path.resolve()) for path in outputs),
    }
    expected_line = json.dumps(
        rows[0],
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8") + b"\n"
    assert journal_path.read_bytes() == expected_line


def test_reservation_failure_is_atomic_and_never_overwrites_existing_path(tmp_path):
    journal_path = tmp_path / "evidence.jsonl"
    first_output = tmp_path / "first.json"
    occupied = tmp_path / "occupied.json"
    occupied.write_bytes(b"owner data")

    with pytest.raises(PathReservationError, match="already exists"):
        LiveEvidenceJournal.create(
            journal_path,
            output_paths=[first_output, occupied],
            identity=_identity(),
            resumable=True,
        )

    assert occupied.read_bytes() == b"owner data"
    assert not journal_path.exists()
    assert not first_output.exists()


def test_existing_journal_is_never_overwritten(tmp_path):
    journal_path = tmp_path / "evidence.jsonl"
    journal_path.write_bytes(b"existing evidence")

    with pytest.raises(PathReservationError, match="already exists"):
        LiveEvidenceJournal.create(
            journal_path,
            output_paths=[],
            identity=_identity(),
            resumable=True,
        )

    assert journal_path.read_bytes() == b"existing evidence"


def test_dangling_symlink_is_an_existing_path_not_a_reservation_target(tmp_path):
    journal_path = tmp_path / "evidence.jsonl"
    symlink_path = tmp_path / "raw.json"
    symlink_target = tmp_path / "uncreated-target.json"
    symlink_path.symlink_to(symlink_target)

    with pytest.raises(PathReservationError, match="already exists"):
        LiveEvidenceJournal.create(
            journal_path,
            output_paths=[symlink_path],
            identity=_identity(),
            resumable=True,
        )

    assert symlink_path.is_symlink()
    assert not symlink_target.exists()
    assert not journal_path.exists()


def test_all_live_event_types_are_hash_chained_and_completion_is_final(tmp_path):
    journal_path, outputs = _paths(tmp_path)
    journal = LiveEvidenceJournal.create(
        journal_path,
        output_paths=outputs,
        identity=_identity(),
        resumable=True,
    )
    event_types = [
        "actor_request",
        "actor_result",
        "actor_error",
        "layer_e_request",
        "layer_e_result",
        "layer_e_error",
        "layer_r_request",
        "layer_r_result",
        "layer_r_error",
        "layer_control_request",
        "layer_control_result",
        "layer_control_error",
        "human_adjudication",
        "job_start",
        "trajectory_result",
        "score_result",
        "job_error",
        "analysis_result",
    ]
    for index, event_type in enumerate(event_types, 1):
        journal.record(event_type, {"call_id": f"C{index:02d}"})
    completion = journal.complete({"status": "complete"})

    assert completion["event_type"] == "completion"
    with pytest.raises(CompletedJournalError):
        journal.record("actor_request", {"call_id": "late"})
    with pytest.raises(CompletedJournalError):
        journal.complete({"status": "duplicate"})
    journal.close()

    snapshot = read_completed_journal(journal_path)
    assert snapshot.completed is True
    assert [row["event_type"] for row in snapshot.events] == [
        "run_start",
        *event_types,
        "completion",
    ]
    for index, row in enumerate(snapshot.events):
        assert row["sequence"] == index
        assert row["event_hash"] == _event_hash(row)
        if index:
            assert row["previous_hash"] == snapshot.events[index - 1]["event_hash"]


def test_record_flushes_and_fsyncs_before_returning_to_external_caller(
    tmp_path, monkeypatch
):
    journal_path, outputs = _paths(tmp_path)
    journal = LiveEvidenceJournal.create(
        journal_path,
        output_paths=outputs,
        identity=_identity(),
        resumable=True,
    )
    order = []
    real_fsync = os.fsync

    def tracking_fsync(fd):
        order.append("fsync")
        return real_fsync(fd)

    monkeypatch.setattr(live_journal.os, "fsync", tracking_fsync)

    journal.record("actor_request", {"call_id": "actor-01"})
    order.append("next_external_call")
    journal.close()

    assert order == ["fsync", "next_external_call"]


@pytest.mark.parametrize(
    "events_before_failure",
    [
        [
            ("actor_request", {"call_id": "actor-N"}),
            ("actor_result", {"call_id": "actor-N", "response_id": "r-N"}),
        ],
        [
            ("layer_e_request", {"call_id": "judge-J01", "judge_id": "J01"}),
            ("layer_e_result", {"call_id": "judge-J01", "label": "fruit"}),
        ],
        [
            ("layer_e_request", {"call_id": "layer-E"}),
            ("layer_e_result", {"call_id": "layer-E", "event": "observable"}),
        ],
        [
            ("layer_r_request", {"call_id": "layer-R"}),
            ("layer_r_result", {"call_id": "layer-R", "label": "vice"}),
        ],
    ],
)
def test_injected_failure_preserves_every_preceding_fsynced_event(
    tmp_path, events_before_failure
):
    journal_path = tmp_path / "evidence.jsonl"

    with pytest.raises(RuntimeError, match="injected failure"):
        with LiveEvidenceJournal.create(
            journal_path,
            output_paths=[tmp_path / "raw.json"],
            identity=_identity(),
            resumable=True,
        ) as journal:
            for event_type, payload in events_before_failure:
                journal.record(event_type, payload)
            raise RuntimeError("injected failure")

    snapshot = validate_journal(journal_path)
    assert snapshot.completed is False
    assert [row["event_type"] for row in snapshot.events] == [
        "run_start",
        *(event_type for event_type, _ in events_before_failure),
    ]


def test_resume_validates_full_chain_and_continues_sequence(tmp_path):
    journal_path, outputs = _paths(tmp_path)
    with LiveEvidenceJournal.create(
        journal_path,
        output_paths=outputs,
        identity=_identity(),
        resumable=True,
    ) as journal:
        first = journal.record("actor_request", {"call_id": "actor-01"})

    with LiveEvidenceJournal.resume(journal_path, identity=_identity()) as resumed:
        second = resumed.record(
            "actor_result", {"call_id": "actor-01", "response_id": "resp-01"}
        )
        resumed.complete({"status": "complete"})

    assert second["sequence"] == 2
    assert second["previous_hash"] == first["event_hash"]
    assert read_completed_journal(journal_path).completed is True


@pytest.mark.parametrize(
    "field",
    ["config_sha256", "source_sha256", "schedule_sha256", "receipt_sha256"],
)
def test_resume_refuses_any_identity_hash_mismatch(tmp_path, field):
    journal_path, outputs = _paths(tmp_path)
    LiveEvidenceJournal.create(
        journal_path,
        output_paths=outputs,
        identity=_identity(),
        resumable=True,
    ).close()
    mismatched = replace(_identity(), **{field: "a" * 64})

    with pytest.raises(ResumeRefusedError, match=field):
        LiveEvidenceJournal.resume(journal_path, identity=mismatched)


def test_resume_refuses_non_resumable_incomplete_run(tmp_path):
    journal_path, outputs = _paths(tmp_path)
    LiveEvidenceJournal.create(
        journal_path,
        output_paths=outputs,
        identity=_identity(),
        resumable=False,
    ).close()

    with pytest.raises(ResumeRefusedError, match="not explicitly resumable"):
        LiveEvidenceJournal.resume(journal_path, identity=_identity())


def test_resume_refuses_completed_run(tmp_path):
    journal_path, outputs = _paths(tmp_path)
    journal = LiveEvidenceJournal.create(
        journal_path,
        output_paths=outputs,
        identity=_identity(),
        resumable=True,
    )
    journal.complete({"status": "complete"})
    journal.close()

    with pytest.raises(CompletedJournalError):
        LiveEvidenceJournal.resume(journal_path, identity=_identity())


def test_resume_refuses_missing_or_replaced_reserved_output(tmp_path):
    journal_path, outputs = _paths(tmp_path)
    LiveEvidenceJournal.create(
        journal_path,
        output_paths=outputs,
        identity=_identity(),
        resumable=True,
    ).close()
    outputs[0].unlink()
    outputs[0].write_bytes(b"replacement")

    with pytest.raises(JournalIntegrityError, match="reservation"):
        LiveEvidenceJournal.resume(journal_path, identity=_identity())


def test_aggregation_refuses_incomplete_journal(tmp_path):
    journal_path, outputs = _paths(tmp_path)
    LiveEvidenceJournal.create(
        journal_path,
        output_paths=outputs,
        identity=_identity(),
        resumable=True,
    ).close()

    with pytest.raises(IncompleteJournalError):
        read_completed_journal(journal_path)


def test_validation_rejects_payload_tampering_even_when_json_is_canonical(tmp_path):
    journal_path, outputs = _paths(tmp_path)
    journal = LiveEvidenceJournal.create(
        journal_path,
        output_paths=outputs,
        identity=_identity(),
        resumable=True,
    )
    journal.record("actor_request", {"call_id": "actor-01"})
    journal.close()
    rows = _decode_rows(journal_path)
    rows[1]["payload"]["call_id"] = "tampered"
    journal_path.write_bytes(
        b"".join(
            json.dumps(
                row,
                ensure_ascii=False,
                allow_nan=False,
                sort_keys=True,
                separators=(",", ":"),
            ).encode("utf-8")
            + b"\n"
            for row in rows
        )
    )

    with pytest.raises(JournalIntegrityError, match="event hash"):
        validate_journal(journal_path)


def test_validation_rejects_rehashed_but_broken_chain(tmp_path):
    journal_path, outputs = _paths(tmp_path)
    journal = LiveEvidenceJournal.create(
        journal_path,
        output_paths=outputs,
        identity=_identity(),
        resumable=True,
    )
    journal.record("actor_request", {"call_id": "actor-01"})
    journal.close()
    rows = _decode_rows(journal_path)
    rows[1]["previous_hash"] = "f" * 64
    rows[1]["event_hash"] = _event_hash(rows[1])
    journal_path.write_bytes(
        b"".join(
            json.dumps(row, sort_keys=True, separators=(",", ":")).encode("utf-8")
            + b"\n"
            for row in rows
        )
    )

    with pytest.raises(JournalIntegrityError, match="previous hash"):
        validate_journal(journal_path)


def test_validation_rejects_non_string_event_type_as_integrity_failure(tmp_path):
    journal_path, outputs = _paths(tmp_path)
    journal = LiveEvidenceJournal.create(
        journal_path,
        output_paths=outputs,
        identity=_identity(),
        resumable=True,
    )
    journal.record("actor_request", {"call_id": "actor-01"})
    journal.close()
    rows = _decode_rows(journal_path)
    rows[1]["event_type"] = ["actor_request"]
    rows[1]["event_hash"] = _event_hash(rows[1])
    journal_path.write_bytes(
        b"".join(
            json.dumps(row, sort_keys=True, separators=(",", ":")).encode("utf-8")
            + b"\n"
            for row in rows
        )
    )

    with pytest.raises(JournalIntegrityError, match="event_type"):
        validate_journal(journal_path)


@pytest.mark.parametrize(
    "payload",
    [
        {"headers": {"Authorization": "Bearer top-secret-token"}},
        {"api_key": "top-secret-token"},
        {"openrouterApiKey": "top-secret-token"},
        {"credentials": "top-secret-token"},
        {"request_body": {"unrelated": "sk-or-v1-abcDEF123456789"}},
    ],
)
def test_secret_material_is_rejected_without_being_written(tmp_path, payload):
    journal_path, outputs = _paths(tmp_path)
    journal = LiveEvidenceJournal.create(
        journal_path,
        output_paths=outputs,
        identity=_identity(),
        resumable=True,
    )

    with pytest.raises(SecretMaterialError, match="secret material") as caught:
        journal.record("actor_request", payload)
    journal.close()

    assert "top-secret" not in str(caught.value)
    assert "sk-or" not in journal_path.read_text(encoding="utf-8")
    assert len(_decode_rows(journal_path)) == 1


def test_normal_token_accounting_is_not_mistaken_for_a_secret(tmp_path):
    journal_path, outputs = _paths(tmp_path)
    with LiveEvidenceJournal.create(
        journal_path,
        output_paths=outputs,
        identity=_identity(),
        resumable=True,
    ) as journal:
        journal.record(
            "actor_result",
            {"usage": {"input_tokens": 120, "output_tokens": 30}},
        )

    assert len(validate_journal(journal_path).events) == 2


def test_invalid_event_or_nonfinite_payload_is_rejected_without_append(tmp_path):
    journal_path, outputs = _paths(tmp_path)
    journal = LiveEvidenceJournal.create(
        journal_path,
        output_paths=outputs,
        identity=_identity(),
        resumable=True,
    )

    with pytest.raises(ValueError, match="event_type"):
        journal.record("arbitrary_event", {})
    with pytest.raises(ValueError, match="canonical JSON"):
        journal.record("actor_result", {"score": float("nan")})
    journal.close()

    assert len(_decode_rows(journal_path)) == 1


def test_partial_or_noncanonical_last_row_fails_closed(tmp_path):
    journal_path, outputs = _paths(tmp_path)
    LiveEvidenceJournal.create(
        journal_path,
        output_paths=outputs,
        identity=_identity(),
        resumable=True,
    ).close()
    with journal_path.open("ab") as stream:
        stream.write(b'{"event_type":"actor_request"}')

    with pytest.raises(JournalIntegrityError, match="newline|canonical|JSON"):
        validate_journal(journal_path)


def test_run_identity_requires_exact_lowercase_sha256_values():
    with pytest.raises(ValueError, match="config_sha256"):
        _identity(config_sha256="not-a-sha256")
    with pytest.raises(ValueError, match="run_id"):
        _identity(run_id=" ")
