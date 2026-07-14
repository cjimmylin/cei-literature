import hashlib
import json
import multiprocessing
from copy import deepcopy

import pytest
import walkworthy.g7_runner as g7_runner

from walkworthy.g7_author_contract import (
    AUTHOR_MODEL,
    AUTHOR_SYSTEM_PROMPT,
    AUTHOR_SYSTEM_PROMPT_SHA256,
    AUTHOR_USER_PROMPT_TEMPLATE,
    AUTHOR_USER_PROMPT_TEMPLATE_SHA256,
    L8_REGEX,
    MEMO_SHA256,
    AuthorCustodyLedger,
    build_author_request,
    build_semantic_review_packets,
    canonical_item_key,
    lint_l1_l9,
    parse_author_response,
    parse_review_submission,
    validate_author_output,
)
from walkworthy.g7_runner import (
    AttemptLedger, ContractStop, ThreadStop, spec_for,
)
from walkworthy.g7_perturbation import (
    ItemRoleManifest, ProtectedNonRole, RoleManifestRow,
)
from walkworthy.models import Administration, Item, Turn


def test_contract_module_exposes_frozen_memo_identity() -> None:
    assert MEMO_SHA256 == "59caaa1c055dd1badd16694e078a91a40b18e4e1ebd9f6d15510f89e9f79b320"


def _item() -> Item:
    return Item(
        id="WW-01-X01", design="01-goodsamaritan", title="Public", area="A",
        difficulty="hard", canary="WALKWORTHY-CANARY-7f3e2026",
        anchors=["pack:claim"], key={"z": "direction", "a": "é"},
        administrations=[Administration(
            label="main", kind="scripted_multi_turn", system="SYSTEM PROTECTED",
            cold_open="Alice opens the Acme Account.",
            turns=[Turn(index=1, text="Alice calls Acme.", branches={
                "zeta": "Alice waits.", "alpha": "Acme answers Alice.",
            })], terminal_ask="Alice closes the Account.",
        )],
    )


def _role_manifest() -> dict:
    return {
        "design": "01-goodsamaritan", "item_id": "WW-01-X01",
        "roles": [{"original": "Alice"}],
        "protected_non_roles": [
            {"literal": "Acme"}, {"literal": "Account"},
        ],
    }


def test_exact_prompt_component_hashes_and_author_payload() -> None:
    assert hashlib.sha256(AUTHOR_SYSTEM_PROMPT.encode()).hexdigest() == AUTHOR_SYSTEM_PROMPT_SHA256
    assert AUTHOR_SYSTEM_PROMPT_SHA256 == "3519c14a172e589cd080d7abcccdc7cfdd2cd8112bb92fe9ef870616cc987b50"
    assert hashlib.sha256(AUTHOR_USER_PROMPT_TEMPLATE.encode()).hexdigest() == AUTHOR_USER_PROMPT_TEMPLATE_SHA256
    assert AUTHOR_USER_PROMPT_TEMPLATE_SHA256 == "546e808b7cba3c33ee69adf53654309790833858cfec1aad22e647b08b8cb9a5"
    assert AUTHOR_SYSTEM_PROMPT.endswith("\n")
    assert AUTHOR_USER_PROMPT_TEMPLATE.endswith("\n")

    request = build_author_request(_item(), _role_manifest())

    assert AUTHOR_MODEL == "mistralai/mistral-large-2512"
    assert request.payload == {
        "model": AUTHOR_MODEL,
        "max_tokens": 4096,
        "provider": {
            "sort": "price", "require_parameters": True, "allow_fallbacks": True,
            "max_price": {"prompt": 0.5, "completion": 1.5},
        },
        "messages": [
            {"role": "system", "content": AUTHOR_SYSTEM_PROMPT},
            {"role": "user", "content": request.user_prompt},
        ],
    }
    assert [field.path.field for field in request.prepared.fields] == [
        "cold_open", "text", "branch", "branch", "terminal_ask",
    ]
    fields = json.loads(request.user_prompt.split("FIELDS:\n", 1)[1])
    assert [entry["field_id"] for entry in fields] == list(range(5))
    assert "{{ITEM_ID}}" not in request.user_prompt
    assert "{{FIELD_COUNT}}" not in request.user_prompt
    assert "{{FIELDS_JSON}}" not in request.user_prompt
    assert "SYSTEM PROTECTED" not in request.user_prompt
    assert all("Alice" not in entry["template"] for entry in fields)
    assert all("Acme" not in entry["template"] for entry in fields)
    assert all("Account" not in entry["template"] for entry in fields)
    assert fields[2]["template"].endswith("answers [[G7_PROTECTED_001]].")


def test_loaded_role_manifest_carries_protected_non_roles_into_templates() -> None:
    manifest = ItemRoleManifest(
        "01-goodsamaritan", "WW-01-X01",
        (RoleManifestRow(
            "01-goodsamaritan", "WW-01-X01", 0, "Alice", "woman", None, (),
        ),),
        (ProtectedNonRole("Acme", "organization", ()),
         ProtectedNonRole("Account", "account", ())),
    )

    request = build_author_request(_item(), manifest)

    templates = tuple(field.template for field in request.prepared.fields)
    assert all("Alice" not in template for template in templates)
    assert all("Acme" not in template for template in templates)
    assert all("Account" not in template for template in templates)


def _author_body(item_id="WW-01-X01", count=5) -> str:
    return json.dumps({
        "item_id": item_id,
        "fields": [{"field_id": index, "paraphrase": f"field {index}"}
                   for index in range(count)],
    })


def test_strict_parser_maps_canonical_field_ids_to_paths() -> None:
    request = build_author_request(_item(), _role_manifest())
    parsed = parse_author_response(_author_body(), _item().id, request.prepared)

    assert parsed.failure is None
    assert tuple(parsed.authored) == tuple(
        field.path for field in request.prepared.fields
    )
    assert list(parsed.authored.values()) == [f"field {index}" for index in range(5)]


@pytest.mark.parametrize(("body", "failure"), [
    ("```json\n{}\n```", "author_nonjson"),
    ('{"item_id":"WW-01-X01","fields":[],"extra":1}', "author_schema_keys"),
    (_author_body("wrong"), "author_item_id"),
    (_author_body(count=4), "author_field_count"),
    ('{"item_id":"WW-01-X01","fields":[{"field_id":0.0,"paraphrase":"x"},'
     '{"field_id":1,"paraphrase":"x"},{"field_id":2,"paraphrase":"x"},'
     '{"field_id":3,"paraphrase":"x"},{"field_id":4,"paraphrase":"x"}]}',
     "author_field_shape"),
    ('{"item_id":"WW-01-X01","fields":[{"field_id":0,"paraphrase":"x"},'
     '{"field_id":0,"paraphrase":"x"},{"field_id":2,"paraphrase":"x"},'
     '{"field_id":3,"paraphrase":"x"},{"field_id":4,"paraphrase":"x"}]}',
     "author_field_ids"),
    ('{"item_id":"WW-01-X01","fields":NaN}', "author_nonjson"),
    ('{"item_id":"WW-01-X01","item_id":"WW-01-X01","fields":[]}',
     "author_schema_keys"),
])
def test_strict_parser_emits_exact_failure_tokens(body, failure) -> None:
    request = build_author_request(_item(), _role_manifest())
    assert parse_author_response(body, _item().id, request.prepared).failure == failure


def _valid_author_body(request, replace_text=None) -> str:
    fields = []
    for index, field in enumerate(request.prepared.fields):
        text = field.template
        if replace_text is not None and index == 0:
            text = replace_text(text)
        fields.append({"field_id": index, "paraphrase": text})
    return json.dumps({"item_id": request.prepared.item_id, "fields": fields})


def _clean_review(packets) -> list:
    return [{"l_check": packet["l_check"], "clean": True} for packet in packets]


def test_gate_a_runs_before_semantic_packet_and_review() -> None:
    item = _item()
    request = build_author_request(item, _role_manifest())
    body = _valid_author_body(
        request, lambda text: text + " [[G7_PROTECTED_999]]"
    )

    result = validate_author_output(item, request.prepared, body)

    assert result.state == "validation_failed"
    assert result.failures == ("unknown_protected_placeholder",)
    assert result.review_packets == ()
    assert result.item is None


def test_exact_public_jimmy_packet_and_fail_closed_explicit_response() -> None:
    item = _item()
    item.admin_mode = "paired"
    request = build_author_request(item, _role_manifest())
    candidate = deepcopy(item)
    candidate.administrations[0].cold_open = "Alice starts the Acme Account."

    packets = build_semantic_review_packets(item, candidate, request.prepared)

    changed = [{
        "field_id": 0,
        "original_text": "Alice opens the Acme Account.",
        "paraphrased_text": "Alice starts the Acme Account.",
    }]
    assert packets == tuple({
        "item_id": item.id,
        "design": item.design,
        "difficulty": "hard",
        "is_paired": True,
        "l_check": check,
        "changed_fields": changed,
        "anchors": ["pack:claim"],
        "key_direction_summary": '{"a":"é","z":"direction"}',
    } for check in ("L1_sense", "L4", "L5", "L9"))
    assert parse_review_submission(packets, None, review_complete=False) is None
    failed = parse_review_submission(
        packets,
        [{"l_check": "L1_sense", "clean": True},
         {"l_check": "L4", "clean": "uncertain"},
         {"l_check": "L5", "clean": True}],
        review_complete=True,
    )
    assert failed == {"L1_sense": True, "L4": False, "L5": True, "L9": False}


def test_exact_l1_l9_and_new_only_no_flags_l8() -> None:
    assert L8_REGEX == r"(?<!\w)(?:[1-3]\s+)?[A-Z][A-Za-z]*\.?(?:\s+[A-Z][A-Za-z]*\.?){0,2}\s+\d{1,3}(?::\d{1,3}(?:[-–]\d{1,3})?)?(?!\w)"
    item = _item()
    item.admin_mode = "paired"
    request = build_author_request(item, _role_manifest())
    candidate = deepcopy(item)
    candidate.anchors = ["changed"]
    candidate.canary = "lost"
    candidate.administrations[0].cold_open = (
        "Bob calls it moral and cites Matt 5:23-24 after 99 days."
    )
    review = {"L1_sense": True, "L4": False, "L5": False, "L9": False}

    lint = lint_l1_l9(item, candidate, request.prepared, review)

    assert tuple(lint) == tuple(f"L{index}" for index in range(1, 10))
    assert lint == {f"L{index}": False for index in range(1, 10)}
    original_with_ref = deepcopy(item)
    original_with_ref.administrations[0].cold_open += " Matt 5:23-24."
    same_ref = deepcopy(original_with_ref)
    prepared_with_ref = build_author_request(
        original_with_ref, _role_manifest()
    ).prepared
    clean_review = {"L1_sense": True, "L4": True, "L5": True, "L9": True}
    assert lint_l1_l9(
        original_with_ref, same_ref, prepared_with_ref, clean_review
    )["L8"] is True


def test_validation_pending_then_all_true_logical_complete() -> None:
    item = _item()
    request = build_author_request(item, _role_manifest())
    body = _valid_author_body(
        request, lambda text: text.replace("opens", "starts")
    )

    pending = validate_author_output(item, request.prepared, body)
    assert pending.state == "validation_pending"
    assert pending.item is None
    completed = validate_author_output(
        item, request.prepared, body,
        review_submission=_clean_review(pending.review_packets),
        review_complete=True,
    )
    assert completed.state == "logical_complete"
    assert completed.failures == ()
    assert completed.item.administrations[0].cold_open == (
        "Alice starts the Acme Account."
    )


def _response(body):
    return {
        "model": AUTHOR_MODEL, "usage": {"cost": 0.001},
        "choices": [{"message": {"content": body}}],
    }


class _InjectedFailure(RuntimeError):
    pass


class _InjectedCrash(BaseException):
    pass


class _FinishFailsBeforeBooking:
    def __init__(self, spend, custody_path):
        self.spend = spend
        self.custody_path = custody_path

    def attempt_snapshot(self, attempt):
        return self.spend.attempt_snapshot(attempt)

    def finish(self, attempt, status, response):
        rows = [json.loads(line) for line in self.custody_path.read_text().splitlines()]
        assert rows[-1]["event"] == "author_transport_custodied"
        assert rows[-1]["response"] == response
        raise _InjectedFailure("before spend finish")


class _CrashAfterSpendFinish:
    def __init__(self, spend):
        self.spend = spend

    def attempt_snapshot(self, attempt):
        return self.spend.attempt_snapshot(attempt)

    def finish(self, attempt, status, response):
        self.spend.finish(attempt, status, response)
        raise _InjectedCrash("after spend finish")


class _MarkFailsAfterDecisionCustody:
    def __init__(self, spend, custody_path):
        self.spend = spend
        self.custody_path = custody_path

    def attempt_snapshot(self, attempt):
        return self.spend.attempt_snapshot(attempt)

    def mark_author_validation(self, attempt, passed):
        rows = [json.loads(line) for line in self.custody_path.read_text().splitlines()]
        assert rows[-1]["event"] == "review_decision_custodied"
        raise _InjectedFailure("before validation mark")


class _CrashAfterValidationMark:
    def __init__(self, spend):
        self.spend = spend

    def attempt_snapshot(self, attempt):
        return self.spend.attempt_snapshot(attempt)

    def mark_author_validation(self, attempt, passed):
        self.spend.mark_author_validation(attempt, passed)
        raise _InjectedCrash("after validation mark")


def _finish_transport_worker(spend_path, custody_path, keys, logical_key,
                             attempt, payload, response, queue):
    try:
        spend = AttemptLedger(spend_path, expected_keys=keys)
        custody = AuthorCustodyLedger(custody_path)
        queue.put(custody.finish_transport(
            spend, logical_key, attempt, payload, 200, response
        ))
    except Exception as exc:  # pragma: no cover - surfaced in parent
        queue.put((type(exc).__name__, str(exc)))


def test_append_only_author_custody_pending_replay_unresolved_and_complete(tmp_path) -> None:
    item = _item()
    request = build_author_request(item, _role_manifest())
    body = _valid_author_body(request)
    spend_path = tmp_path / "spend.jsonl"
    custody_path = tmp_path / "author-custody.jsonl"
    spend = AttemptLedger(spend_path, expected_keys=(item.id, "complete-key"))
    custody = AuthorCustodyLedger(custody_path)
    spec = spec_for("paraphrase_author", AUTHOR_MODEL)

    first = spend.begin(item.id, spec, request.payload)
    assert custody.finish_transport(
        spend, item.id, first, request.payload, 200, _response(body)
    ) == "validation_pending"
    pending = validate_author_output(item, request.prepared, body)
    assert custody.record_validation(item.id, first, pending, spend) == "validation_pending"
    with pytest.raises(ThreadStop, match="validation pending"):
        spend.begin(item.id, spec, request.payload)

    failed = validate_author_output(
        item, request.prepared, body, review_submission=[], review_complete=True
    )
    assert custody.record_validation(item.id, first, failed, spend) == "replay_required"
    second = spend.begin(item.id, spec, request.payload)
    assert custody.finish_transport(
        spend, item.id, second, request.payload, 200, _response(body)
    ) == "validation_pending"
    assert custody.record_validation(item.id, second, failed, spend) == "unresolved"
    with pytest.raises(ThreadStop, match="exhausted"):
        spend.begin(item.id, spec, request.payload)

    attempt = spend.begin("complete-key", spec, request.payload)
    custody.finish_transport(
        spend, "complete-key", attempt, request.payload, 200, _response(body)
    )
    completed = validate_author_output(
        item, request.prepared, body,
        review_submission=_clean_review(pending.review_packets), review_complete=True,
    )
    assert custody.record_validation(
        "complete-key", attempt, completed, spend
    ) == "complete"
    assert "logical_complete" in custody_path.read_text()
    custody_rows = [json.loads(line) for line in custody_path.read_text().splitlines()]
    assert custody_rows[0]["response"]["choices"][0]["message"]["content"] == body
    decision_rows = [row for row in custody_rows
                     if row["event"] == "review_decision_custodied"]
    assert decision_rows[-1]["review_submission"] == _clean_review(pending.review_packets)
    assert body not in spend_path.read_text()


def test_duplicate_malformed_required_review_poison_stays_false() -> None:
    item = _item()
    request = build_author_request(item, _role_manifest())
    body = _valid_author_body(request)
    pending = validate_author_output(item, request.prepared, body)
    review = [
        {"l_check": "L1_sense", "clean": True},
        {"l_check": "L5", "clean": True},
        {"l_check": "L5", "clean": "uncertain"},
        {"l_check": "L9", "clean": True},
    ]

    parsed = parse_review_submission(
        pending.review_packets, review, review_complete=True
    )
    result = validate_author_output(
        item, request.prepared, body,
        review_submission=review, review_complete=True,
    )

    assert parsed["L5"] is False
    assert result.state == "validation_failed"
    assert "L5" in result.failures


def test_pending_review_packets_are_append_only_custodied_before_return(tmp_path) -> None:
    item = _item()
    request = build_author_request(item, _role_manifest())
    body = _valid_author_body(request)
    spend_path = tmp_path / "spend.jsonl"
    custody_path = tmp_path / "author-custody.jsonl"
    spend = AttemptLedger(spend_path, expected_keys=(item.id,))
    custody = AuthorCustodyLedger(custody_path)
    spec = spec_for("paraphrase_author", AUTHOR_MODEL)
    attempt = spend.begin(item.id, spec, request.payload)
    custody.finish_transport(
        spend, item.id, attempt, request.payload, 200, _response(body)
    )
    pending = validate_author_output(item, request.prepared, body)

    assert custody.record_validation(
        item.id, attempt, pending, spend
    ) == "validation_pending"

    rows = [json.loads(line) for line in custody_path.read_text().splitlines()]
    assert rows[-1]["event"] == "review_packets_custodied"
    assert rows[-1]["logical_key"] == item.id
    assert rows[-1]["attempt_id"] == attempt
    assert rows[-1]["review_packets"] == list(pending.review_packets)
    assert len(rows[-1]["packets_sha256"]) == 64
    spend_text = spend_path.read_text()
    assert '"event":"validation_pending"' in spend_text
    assert '"event":"logical_complete"' not in spend_text
    assert body not in spend_text


def test_transport_body_is_custodied_before_injected_spend_finish_failure(tmp_path) -> None:
    item = _item()
    request = build_author_request(item, _role_manifest())
    body = _valid_author_body(request)
    spend = AttemptLedger(tmp_path / "spend.jsonl", expected_keys=(item.id,))
    custody_path = tmp_path / "custody.jsonl"
    custody = AuthorCustodyLedger(custody_path)
    attempt = spend.begin(
        item.id, spec_for("paraphrase_author", AUTHOR_MODEL), request.payload
    )
    injected = _FinishFailsBeforeBooking(spend, custody_path)

    with pytest.raises(_InjectedFailure, match="before spend finish"):
        custody.finish_transport(
            injected, item.id, attempt, request.payload, 200, _response(body)
        )

    rows = [json.loads(line) for line in custody_path.read_text().splitlines()]
    assert rows[-1]["response"]["choices"][0]["message"]["content"] == body
    assert spend.attempt_snapshot(attempt)["finish"] is None


def test_custody_refuses_already_finished_spend_without_prior_body_intent(tmp_path) -> None:
    item = _item()
    request = build_author_request(item, _role_manifest())
    body = _valid_author_body(request)
    spend = AttemptLedger(tmp_path / "spend.jsonl", expected_keys=(item.id,))
    custody = AuthorCustodyLedger(tmp_path / "custody.jsonl")
    attempt = spend.begin(
        item.id, spec_for("paraphrase_author", AUTHOR_MODEL), request.payload
    )
    spend.finish(attempt, 200, _response(body))

    with pytest.raises(ContractStop, match="finished before body custody"):
        custody.finish_transport(
            spend, item.id, attempt, request.payload, 200, _response(body)
        )


def test_transport_reconciles_crash_after_spend_finish_and_rejects_conflicts(tmp_path) -> None:
    item = _item()
    request = build_author_request(item, _role_manifest())
    body = _valid_author_body(request)
    response = _response(body)
    spend = AttemptLedger(tmp_path / "spend.jsonl", expected_keys=(item.id,))
    custody_path = tmp_path / "custody.jsonl"
    custody = AuthorCustodyLedger(custody_path)
    attempt = spend.begin(
        item.id, spec_for("paraphrase_author", AUTHOR_MODEL), request.payload
    )

    with pytest.raises(_InjectedCrash, match="after spend finish"):
        custody.finish_transport(
            _CrashAfterSpendFinish(spend), item.id, attempt,
            request.payload, 200, response,
        )
    assert [json.loads(line)["event"] for line in custody_path.read_text().splitlines()] == [
        "author_transport_custodied"
    ]

    assert custody.finish_transport(
        spend, item.id, attempt, request.payload, 200, response
    ) == "validation_pending"
    line_count = len(custody_path.read_text().splitlines())
    assert custody.finish_transport(
        spend, item.id, attempt, request.payload, 200, response
    ) == "validation_pending"
    assert len(custody_path.read_text().splitlines()) == line_count

    with pytest.raises(ContractStop, match="custody conflict"):
        custody.finish_transport(
            spend, item.id, attempt, request.payload, 200,
            _response(body + " changed"),
        )
    changed_payload = deepcopy(request.payload)
    changed_payload["messages"][-1]["content"] += " changed"
    with pytest.raises(ContractStop, match="payload"):
        custody.finish_transport(
            spend, item.id, attempt, changed_payload, 200, response
        )
    with pytest.raises(ContractStop, match="logical key"):
        custody.finish_transport(
            spend, "wrong-key", attempt, request.payload, 200, response
        )


def test_successful_finish_crash_before_pending_reconciles_without_rebooking(
    tmp_path, monkeypatch,
) -> None:
    item = _item()
    request = build_author_request(item, _role_manifest())
    body = _valid_author_body(request)
    response = _response(body)
    spend_path = tmp_path / "spend.jsonl"
    custody_path = tmp_path / "custody.jsonl"
    spend = AttemptLedger(spend_path, expected_keys=(item.id,))
    custody = AuthorCustodyLedger(custody_path)
    attempt = spend.begin(
        item.id, spec_for("paraphrase_author", AUTHOR_MODEL), request.payload
    )
    real_append = g7_runner._append

    def crash_after_finished(path, event):
        real_append(path, event)
        if event.get("event") == "attempt_finished":
            raise _InjectedCrash("between finish and validation pending")

    monkeypatch.setattr(g7_runner, "_append", crash_after_finished)
    with pytest.raises(_InjectedCrash, match="between finish and validation pending"):
        custody.finish_transport(
            spend, item.id, attempt, request.payload, 200, response
        )
    monkeypatch.setattr(g7_runner, "_append", real_append)

    resumed = AttemptLedger(spend_path, expected_keys=(item.id,))
    interrupted = resumed.attempt_snapshot(attempt)
    assert interrupted["finish"]["failure"] is None
    assert interrupted["validation"] is None
    assert interrupted["finish"]["booked_usd"] == "0.001"
    custody_rows = [json.loads(line) for line in custody_path.read_text().splitlines()]
    assert custody_rows[-1]["response"] == response
    with pytest.raises(ContractStop, match="duplicate completed"):
        resumed.begin(
            item.id, spec_for("paraphrase_author", AUTHOR_MODEL), request.payload
        )

    assert custody.finish_transport(
        resumed, item.id, attempt, request.payload, 200, response
    ) == "validation_pending"
    reconciled = resumed.attempt_snapshot(attempt)
    assert reconciled["validation"]["event"] == "validation_pending"
    spend_events = [json.loads(line) for line in spend_path.read_text().splitlines()]
    assert sum(row["event"] == "attempt_finished" for row in spend_events) == 1
    assert sum(row["event"] == "validation_pending" for row in spend_events) == 1
    assert resumed.actual_usd == spend.actual_usd

    pending = validate_author_output(item, request.prepared, body)
    assert custody.record_validation(
        item.id, attempt, pending, resumed
    ) == "validation_pending"
    line_counts = (
        len(spend_path.read_text().splitlines()),
        len(custody_path.read_text().splitlines()),
    )
    assert custody.finish_transport(
        resumed, item.id, attempt, request.payload, 200, response
    ) == "validation_pending"
    assert (
        len(spend_path.read_text().splitlines()),
        len(custody_path.read_text().splitlines()),
    ) == line_counts


def test_failed_transport_body_is_custodied_without_validation_pending(tmp_path) -> None:
    item = _item()
    request = build_author_request(item, _role_manifest())
    spend = AttemptLedger(tmp_path / "spend.jsonl", expected_keys=(item.id,))
    custody_path = tmp_path / "custody.jsonl"
    custody = AuthorCustodyLedger(custody_path)
    attempt = spend.begin(
        item.id, spec_for("paraphrase_author", AUTHOR_MODEL), request.payload
    )
    response = {"error": "bad surrogate \ud800"}

    assert custody.finish_transport(
        spend, item.id, attempt, request.payload, 503, response
    ) == "replay_required"

    rows = [json.loads(line) for line in custody_path.read_text().splitlines()]
    assert rows[0]["response"] == response
    assert rows[-1]["outcome"] == "replay_required"
    assert all(row["event"] != "validation_pending" for row in rows)

    replay = spend.begin(
        item.id, spec_for("paraphrase_author", AUTHOR_MODEL), request.payload
    )
    second_response = {"error": "second failed body"}
    with pytest.raises(ThreadStop, match="second failure"):
        custody.finish_transport(
            spend, item.id, replay, request.payload, 503, second_response
        )
    rows = [json.loads(line) for line in custody_path.read_text().splitlines()]
    assert rows[-2]["response"] == second_response
    assert rows[-1]["outcome"] == "thread_stop"
    assert all(row["event"] != "validation_pending" for row in rows)


def test_review_decision_is_custodied_before_mark_and_reconciles_retry(tmp_path) -> None:
    item = _item()
    request = build_author_request(item, _role_manifest())
    body = _valid_author_body(request)
    spend = AttemptLedger(tmp_path / "spend.jsonl", expected_keys=(item.id,))
    custody_path = tmp_path / "custody.jsonl"
    custody = AuthorCustodyLedger(custody_path)
    attempt = spend.begin(
        item.id, spec_for("paraphrase_author", AUTHOR_MODEL), request.payload
    )
    custody.finish_transport(
        spend, item.id, attempt, request.payload, 200, _response(body)
    )
    pending = validate_author_output(item, request.prepared, body)
    custody.record_validation(item.id, attempt, pending, spend)
    completed = validate_author_output(
        item, request.prepared, body,
        review_submission=_clean_review(pending.review_packets),
        review_complete=True,
    )

    with pytest.raises(_InjectedFailure, match="before validation mark"):
        custody.record_validation(
            item.id, attempt, completed,
            _MarkFailsAfterDecisionCustody(spend, custody_path),
        )
    assert spend.attempt_snapshot(attempt)["validation"]["event"] == "validation_pending"

    assert custody.record_validation(
        item.id, attempt, completed, spend
    ) == "complete"
    events = [json.loads(line)["event"]
              for line in custody_path.read_text().splitlines()]
    assert events[-2:] == ["review_decision_custodied", "validation_outcome"]
    line_count = len(events)
    assert custody.record_validation(
        item.id, attempt, completed, spend
    ) == "complete"
    assert len(custody_path.read_text().splitlines()) == line_count


def test_review_reconciles_crash_after_spend_mark_before_custody_outcome(tmp_path) -> None:
    item = _item()
    request = build_author_request(item, _role_manifest())
    body = _valid_author_body(request)
    spend = AttemptLedger(tmp_path / "spend.jsonl", expected_keys=(item.id,))
    custody_path = tmp_path / "custody.jsonl"
    custody = AuthorCustodyLedger(custody_path)
    attempt = spend.begin(
        item.id, spec_for("paraphrase_author", AUTHOR_MODEL), request.payload
    )
    custody.finish_transport(
        spend, item.id, attempt, request.payload, 200, _response(body)
    )
    pending = validate_author_output(item, request.prepared, body)
    custody.record_validation(item.id, attempt, pending, spend)
    completed = validate_author_output(
        item, request.prepared, body,
        review_submission=_clean_review(pending.review_packets),
        review_complete=True,
    )

    with pytest.raises(_InjectedCrash, match="after validation mark"):
        custody.record_validation(
            item.id, attempt, completed, _CrashAfterValidationMark(spend)
        )
    assert [json.loads(line)["event"]
            for line in custody_path.read_text().splitlines()][-1] == (
                "review_decision_custodied"
            )
    assert spend.attempt_snapshot(attempt)["validation"]["event"] == "logical_complete"

    assert custody.record_validation(
        item.id, attempt, completed, spend
    ) == "complete"
    assert json.loads(custody_path.read_text().splitlines()[-1])["event"] == (
        "validation_outcome"
    )


def test_process_safe_custody_keeps_two_concurrent_attempts_valid_jsonl(tmp_path) -> None:
    item = _item()
    request = build_author_request(item, _role_manifest())
    keys = ("one", "two")
    spend_path = tmp_path / "spend.jsonl"
    custody_path = tmp_path / "custody.jsonl"
    spend = AttemptLedger(spend_path, expected_keys=keys)
    spec = spec_for("paraphrase_author", AUTHOR_MODEL)
    attempts = [spend.begin(key, spec, request.payload) for key in keys]
    context = multiprocessing.get_context("fork")
    queue = context.Queue()
    processes = [context.Process(
        target=_finish_transport_worker,
        args=(spend_path, custody_path, keys, key, attempt, request.payload,
              _response(_valid_author_body(request)), queue),
    ) for key, attempt in zip(keys, attempts)]
    for process in processes:
        process.start()
    results = [queue.get(timeout=10) for _process in processes]
    for process in processes:
        process.join(timeout=10)
        assert process.exitcode == 0

    assert sorted(results) == ["validation_pending", "validation_pending"]
    rows = [json.loads(line) for line in custody_path.read_text().splitlines()]
    assert len(rows) == 4
    assert {row["attempt_id"] for row in rows} == set(attempts)
    AuthorCustodyLedger(custody_path)


def test_spend_loader_rejects_boolean_validation_attempt_id(tmp_path) -> None:
    item = _item()
    request = build_author_request(item, _role_manifest())
    path = tmp_path / "spend.jsonl"
    spend = AttemptLedger(path, expected_keys=(item.id,))
    attempt = spend.begin(
        item.id, spec_for("paraphrase_author", AUTHOR_MODEL), request.payload
    )
    spend.finish(attempt, 200, _response(_valid_author_body(request)))
    rows = [json.loads(line) for line in path.read_text().splitlines()]
    rows[-1]["attempt_id"] = True
    path.write_text("".join(json.dumps(row, separators=(",", ":")) + "\n"
                            for row in rows))

    with pytest.raises(ContractStop, match="validation event"):
        AttemptLedger(path, expected_keys=(item.id,))


def test_pairing_uses_item_metadata_not_whole_design() -> None:
    item = _item()
    item.id = "WW-04-B05"
    item.design = "04-innerweight"
    item.admin_mode = "single"
    item.pair_id = None
    manifest = _role_manifest()
    manifest["item_id"] = item.id
    manifest["design"] = item.design
    request = build_author_request(item, manifest)

    unpaired = build_semantic_review_packets(item, deepcopy(item), request.prepared)
    assert "L4" not in {packet["l_check"] for packet in unpaired}

    item.admin_mode = "paired"
    paired_request = build_author_request(item, manifest)
    paired = build_semantic_review_packets(
        item, deepcopy(item), paired_request.prepared
    )
    assert "L4" in {packet["l_check"] for packet in paired}
