import json
import re
import threading
from copy import deepcopy

import pytest

from walkworthy.g7_author_contract import AUTHOR_MODEL, AuthorCustodyLedger
from walkworthy.g7_author_stage import (
    AuthorStageSurface,
    _prepare_surface,
    _registration,
    build_production_author_surface,
    run_author_surface_first_attempts,
)
from walkworthy.g7_runner import (
    HARD_NTE_USD,
    PRODUCTION_MANIFEST_SHA256,
    ROLE_MANIFEST_SHA256,
    AttemptLedger,
    ContractStop,
    write_once_json,
)
from walkworthy.models import Administration, Item, Turn


def _item(index: int) -> Item:
    return Item(
        id=f"WW-01-X{index:02d}", design="01-goodsamaritan", title="Public",
        area="A", difficulty="hard", canary="WALKWORTHY-CANARY-7f3e2026",
        anchors=["pack:claim"], key={"direction": "same"},
        administrations=[Administration(
            label="main", kind="scripted_multi_turn", system="SYSTEM",
            cold_open=f"Alice opens case {index}.",
            turns=[Turn(index=1, text="Alice considers the case.")],
            terminal_ask="Alice answers.",
        )],
    )


def _surface(size=4) -> AuthorStageSurface:
    items = tuple(_item(index) for index in range(1, size + 1))
    roles = tuple({
        "design": item.design, "item_id": item.id,
        "roles": ({"original": "Alice"},), "protected_non_roles": (),
    } for item in items)
    return AuthorStageSurface(
        items=items, role_manifests=roles,
        manifest_sha256=PRODUCTION_MANIFEST_SHA256,
        role_manifest_sha256=ROLE_MANIFEST_SHA256,
    )


def _valid_body(payload):
    user = payload["messages"][1]["content"]
    item_id = re.search(r"^ITEM_ID: (.+)$", user, re.MULTILINE).group(1)
    fields = json.loads(user.split("FIELDS:\n", 1)[1])
    return json.dumps({
        "item_id": item_id,
        "fields": [
            {"field_id": row["field_id"], "paraphrase": row["template"]}
            for row in fields
        ],
    })


def _response(payload):
    return {
        "model": AUTHOR_MODEL,
        "usage": {"cost": 0.001},
        "choices": [{"message": {"content": _valid_body(payload)}}],
    }


def _initialized_run(tmp_path, size=2):
    surface = _surface(size)
    items, keys, requests, spec = _prepare_surface(surface)
    out = tmp_path / "resumed-run"
    out.mkdir()
    write_once_json(
        out / "author-registration.json",
        _registration(surface, keys, spec.max_missing_cost * len(keys)),
    )
    spend = AttemptLedger(
        out / "author-attempts.jsonl", expected_keys=keys,
        hard_nte_usd=HARD_NTE_USD, planned_cap=len(keys),
        replay_cap=len(keys), post_cap=2 * len(keys), max_concurrency=2,
    )
    custody = AuthorCustodyLedger(out / "author-custody.jsonl")
    return surface, items, requests, spec, out, spend, custody


class _InjectedCrash(RuntimeError):
    pass


class _FailBeforeSpendFinish:
    def __init__(self, spend):
        self.spend = spend

    def attempt_snapshot(self, attempt):
        return self.spend.attempt_snapshot(attempt)

    def finish(self, _attempt, _status, _response):
        raise _InjectedCrash("before spend finish")


class _CrashAfterSpendFinish:
    def __init__(self, spend):
        self.spend = spend

    def attempt_snapshot(self, attempt):
        return self.spend.attempt_snapshot(attempt)

    def finish(self, attempt, status, response):
        self.spend.finish(attempt, status, response)
        raise _InjectedCrash("after spend finish")


class RecordingValidTransport:
    def __init__(self, custody_path=None):
        self.calls = []
        self.custody_path = custody_path
        self.saw_packet_before_call = []

    def __call__(self, _url, _headers, payload, timeout=None):
        self.calls.append((deepcopy(payload), timeout))
        text = (self.custody_path.read_text() if self.custody_path
                and self.custody_path.exists() else "")
        self.saw_packet_before_call.append(
            '"event":"review_packets_custodied"' in text
        )
        return 200, _response(payload)


class FakeTransport:
    def __init__(self):
        self.calls = []
        self.active = 0
        self.max_active = 0
        self.lock = threading.Lock()
        self.barrier = threading.Barrier(2)

    def __call__(self, url, headers, payload, timeout=None):
        with self.lock:
            self.calls.append((url, deepcopy(headers), deepcopy(payload), timeout))
            self.active += 1
            self.max_active = max(self.max_active, self.active)
        self.barrier.wait(timeout=5)
        item_id = re.search(
            r"^ITEM_ID: (.+)$", payload["messages"][1]["content"], re.MULTILINE
        ).group(1)
        suffix = int(item_id.rsplit("X", 1)[1])
        body = _valid_body(payload)
        if suffix == 2:
            body = "{}"
        if suffix == 3:
            result = (503, {"error": "offline fake"})
        else:
            result = (200, {
                "model": "wrong/model" if suffix == 4 else AUTHOR_MODEL,
                "usage": {"cost": 0.001},
                "choices": [{"message": {"content": body}}],
            })
        with self.lock:
            self.active -= 1
        return result


def test_production_surface_is_exact_public_73_and_frozen_hashes(benchmark_root):
    surface = build_production_author_surface(benchmark_root)

    assert len(surface.items) == len(surface.role_manifests) == 73
    assert tuple(item.id for item in surface.items) == tuple(sorted(
        (item.id for item in surface.items),
        key=lambda item_id: next(
            (item.design, item.id) for item in surface.items if item.id == item_id
        ),
    ))
    assert surface.manifest_sha256 == PRODUCTION_MANIFEST_SHA256
    assert surface.role_manifest_sha256 == ROLE_MANIFEST_SHA256


def test_first_attempt_stage_custodies_failures_packets_and_resumes_without_calls(tmp_path):
    transport = FakeTransport()
    out = tmp_path / "new-run"

    checkpoint = run_author_surface_first_attempts(
        _surface(), out, "TEST-KEY-MUST-NOT-PERSIST", transport, max_workers=2
    )

    assert len(transport.calls) == 4
    assert len({call[2]["messages"][1]["content"] for call in transport.calls}) == 4
    assert transport.max_active == 2
    assert all(call[0] == "https://openrouter.ai/api/v1/chat/completions"
               for call in transport.calls)
    assert all(call[1]["Authorization"] == "Bearer TEST-KEY-MUST-NOT-PERSIST"
               for call in transport.calls)
    assert checkpoint["planned"] == checkpoint["attempts"] == checkpoint["posts"] == 4
    assert checkpoint["validation_pending"] == 1
    assert checkpoint["replay_required"] == checkpoint["unresolved"] == 3
    assert checkpoint["pending_item_ids"] == ["WW-01-X01"]
    assert checkpoint["replay_item_ids"] == ["WW-01-X02", "WW-01-X03", "WW-01-X04"]
    assert checkpoint["actual_usd"] == "0.003"
    assert checkpoint["reserved_usd"] == "0.018144000"
    assert checkpoint["complete"] is False
    assert checkpoint["status"] == "validation_pending_jimmy"
    assert checkpoint["max_author_envelope_usd"] == "0.072576000"
    assert checkpoint["remaining_global_nte_usd"] == "29.978856000"

    spend_text = (out / "author-attempts.jsonl").read_text()
    custody_text = (out / "author-custody.jsonl").read_text()
    assert "TEST-KEY-MUST-NOT-PERSIST" not in spend_text
    assert "TEST-KEY-MUST-NOT-PERSIST" not in custody_text
    assert '"choices"' not in spend_text
    assert '"choices"' in custody_text
    assert spend_text.count('"event":"attempt_started"') == 4
    assert '"event":"validation_failed"' in spend_text

    packet_export = json.loads(
        (out / "jimmy-semantic-review-packets.json").read_text()
    )
    assert [(row["item_id"], row["attempt_id"])
            for row in packet_export["items"]] == [("WW-01-X01", 1)]
    assert packet_export["items"][0]["review_packets"]
    assert "response" not in json.dumps(packet_export)

    assert run_author_surface_first_attempts(
        _surface(), out, "SECOND-KEY", transport, max_workers=2
    ) == checkpoint
    assert len(transport.calls) == 4


def test_preflight_rejects_bad_worker_count_without_creating_run_dir(tmp_path):
    out = tmp_path / "must-not-exist"
    with pytest.raises(ContractStop, match="max_workers"):
        run_author_surface_first_attempts(
            _surface(1), out, "key", lambda *_args, **_kwargs: None,
            max_workers=3,
        )
    assert not out.exists()


def test_transport_exception_custody_never_persists_key_or_exception_message(tmp_path):
    out = tmp_path / "single-worker-run"
    calls = []

    def raising_transport(_url, headers, _payload, timeout=None):
        calls.append(timeout)
        raise RuntimeError(f"transport exposed {headers['Authorization']}")

    checkpoint = run_author_surface_first_attempts(
        _surface(1), out, "SECRET-KEY", raising_transport, max_workers=1
    )

    assert calls == [120.0]
    assert checkpoint["replay_required"] == checkpoint["unresolved"] == 1
    assert checkpoint["reserved_usd"] == "0.018144000"
    assert "SECRET-KEY" not in (out / "author-custody.jsonl").read_text()
    assert "transport exposed" not in (out / "author-custody.jsonl").read_text()


def test_noncallable_transport_stops_before_run_directory_creation(tmp_path):
    out = tmp_path / "must-not-exist"

    with pytest.raises(ContractStop, match="transport must be callable"):
        run_author_surface_first_attempts(
            _surface(1), out, "key", object(), max_workers=1
        )

    assert not out.exists()


def test_started_without_body_custody_stops_before_any_new_post_or_checkpoint(tmp_path):
    surface, items, requests, spec, out, spend, _custody = _initialized_run(tmp_path)
    spend.begin(items[0].id, spec, requests[0].payload)
    transport = RecordingValidTransport()

    with pytest.raises(ContractStop, match="started attempt lacks body custody"):
        run_author_surface_first_attempts(
            surface, out, "key", transport, max_workers=1
        )

    assert transport.calls == []
    assert not (out / "author-checkpoint.json").exists()
    assert not (out / "jimmy-semantic-review-packets.json").exists()


def test_body_custody_without_spend_finish_reconciles_before_only_missing_post(tmp_path):
    surface, items, requests, spec, out, spend, custody = _initialized_run(tmp_path)
    attempt = spend.begin(items[0].id, spec, requests[0].payload)
    with pytest.raises(_InjectedCrash, match="before spend finish"):
        custody.finish_transport(
            _FailBeforeSpendFinish(spend), items[0].id, attempt,
            requests[0].payload, 200, _response(requests[0].payload),
        )
    transport = RecordingValidTransport(out / "author-custody.jsonl")

    checkpoint = run_author_surface_first_attempts(
        surface, out, "key", transport, max_workers=1
    )

    assert len(transport.calls) == 1
    assert "WW-01-X02" in transport.calls[0][0]["messages"][1]["content"]
    assert transport.saw_packet_before_call == [True]
    assert checkpoint["validation_pending"] == 2
    assert spend.attempt_snapshot(attempt)["finish"] is not None


def test_spend_finish_without_custody_outcome_reconciles_before_missing_post(tmp_path):
    surface, items, requests, spec, out, spend, custody = _initialized_run(tmp_path)
    attempt = spend.begin(items[0].id, spec, requests[0].payload)
    with pytest.raises(_InjectedCrash, match="after spend finish"):
        custody.finish_transport(
            _CrashAfterSpendFinish(spend), items[0].id, attempt,
            requests[0].payload, 200, _response(requests[0].payload),
        )
    transport = RecordingValidTransport(out / "author-custody.jsonl")

    checkpoint = run_author_surface_first_attempts(
        surface, out, "key", transport, max_workers=1
    )

    assert len(transport.calls) == 1
    assert transport.saw_packet_before_call == [True]
    assert checkpoint["validation_pending"] == 2
    custody_text = (out / "author-custody.jsonl").read_text()
    assert custody_text.count('"event":"author_transport_outcome"') == 2


def test_pending_outcome_without_packet_recovers_packet_before_missing_post(tmp_path):
    surface, items, requests, spec, out, spend, custody = _initialized_run(tmp_path)
    attempt = spend.begin(items[0].id, spec, requests[0].payload)
    assert custody.finish_transport(
        spend, items[0].id, attempt, requests[0].payload,
        200, _response(requests[0].payload),
    ) == "validation_pending"
    transport = RecordingValidTransport(out / "author-custody.jsonl")

    checkpoint = run_author_surface_first_attempts(
        surface, out, "key", transport, max_workers=1
    )

    assert len(transport.calls) == 1
    assert transport.saw_packet_before_call == [True]
    assert checkpoint["validation_pending"] == 2
    packet_export = json.loads(
        (out / "jimmy-semantic-review-packets.json").read_text()
    )
    assert [row["item_id"] for row in packet_export["items"]] == [
        "WW-01-X01", "WW-01-X02",
    ]
