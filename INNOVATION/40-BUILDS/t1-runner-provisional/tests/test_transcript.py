"""Transcript logger tests — append-only JSONL, full request+response, parseable."""

import json

from t1_runner import (ModelRequest, ModelResponse, ResponseStatus,
                       TranscriptLogger, PROVENANCE_CLASS)


def _resp(text="OK", status=ResponseStatus.OK, item_id="q1"):
    return ModelResponse(
        text=text, status=status, backend="anthropic_cli",
        model_id_reported="claude-opus-4-8", cli_version="2.1.183",
        latency_s=1.23, request=ModelRequest(prompt="Reply OK", item_id=item_id,
                                             params={"model": "opus"}),
        raw_output='[{"type":"result","result":"OK"}]',
        argv=["claude", "-p", "Reply OK", "--model", "opus"])


def test_transcript_writes_and_parses(tmp_path):
    log = TranscriptLogger(str(tmp_path), runid="test1")
    log.log(_resp())
    log.log(_resp(text="hedge", status=ResponseStatus.REFUSAL, item_id="q2"))
    assert log.count == 2
    records = log.read_all()
    assert len(records) == 2
    # full request preserved
    assert records[0]["request"]["prompt"] == "Reply OK"
    assert records[0]["request"]["argv"][0] == "claude"
    assert records[0]["request"]["params"] == {"model": "opus"}
    # full raw response preserved
    assert records[0]["response"]["raw_output"] == '[{"type":"result","result":"OK"}]'
    assert records[0]["response"]["latency_s"] == 1.23
    # provenance stamped
    assert records[0]["provenance"]["provenance_class"] == PROVENANCE_CLASS
    assert records[0]["provenance"]["model_id_reported"] == "claude-opus-4-8"
    assert records[0]["provenance"]["cli_version"] == "2.1.183"
    assert records[1]["response"]["status"] == "refusal"


def test_transcript_is_append_only(tmp_path):
    log = TranscriptLogger(str(tmp_path), runid="test2")
    log.log(_resp())
    # a second logger to same file/runid must append, not truncate
    log2 = TranscriptLogger(str(tmp_path), runid="test2")
    log2.log(_resp(item_id="q2"))
    records = log2.read_all()
    assert len(records) == 2


def test_transcript_filename_has_date_prefix(tmp_path):
    log = TranscriptLogger(str(tmp_path), runid="abc")
    assert log.path.endswith("20260709-abc.jsonl")


def test_every_line_is_valid_json(tmp_path):
    log = TranscriptLogger(str(tmp_path), runid="jsonl")
    for i in range(5):
        log.log(_resp(item_id=f"q{i}"))
    with open(log.path) as fh:
        lines = [l for l in fh if l.strip()]
    assert len(lines) == 5
    for l in lines:
        json.loads(l)  # must not raise
