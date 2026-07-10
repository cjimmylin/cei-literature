"""Offline contract tests for the single-vendor OpenRouter diagnostic.

Every client and catalog response in this module is injected.  These tests
must never make a network call or sleep.
"""

from copy import deepcopy
import hashlib
import json
from pathlib import Path
import sys

import pytest


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

CONFIG_PATH = ROOT / "configs/openrouter-gpt55-54-54mini-forced-diagnostic.json"
R2_CONFIG_PATH = ROOT / "configs/openrouter-gpt55-54-54mini-forced-diagnostic-r2.json"
BANK_PATH = ROOT / "itembank/bank/p1-private.jsonl"
GOLD_PATH = ROOT / "itembank/gold/p1-private.gold.jsonl"


def _jsonl_bytes(payload):
    return [json.loads(line) for line in payload.decode("utf-8").splitlines() if line]


def _frozen_inputs(config_path=CONFIG_PATH):
    config_bytes = Path(config_path).read_bytes()
    bank_bytes = BANK_PATH.read_bytes()
    gold_bytes = GOLD_PATH.read_bytes()
    return (
        json.loads(config_bytes),
        _jsonl_bytes(bank_bytes),
        _jsonl_bytes(gold_bytes),
        config_bytes,
        bank_bytes,
        gold_bytes,
    )


def _catalog(config):
    return {
        "verified": True,
        "model_ids": [row["model_id"] for row in config["model_roster"]],
    }


class FakeClient:
    def __init__(self, roster_row, responder=None, *, usage=True, mutate=False):
        self.model_id = roster_row["model_id"]
        self.family = roster_row["family"]
        self.vendor = roster_row["vendor"]
        self.calls = []
        self._responder = responder or (lambda client, request, seed: "A")
        self._last_call_metadata = None
        self._usage = usage
        self._mutate = mutate

    @property
    def last_call_metadata(self):
        return deepcopy(self._last_call_metadata)

    def generate(self, request, *, seed):
        snapshot = deepcopy(request)
        self.calls.append((snapshot, seed))
        if self._mutate:
            request["messages"][0]["content"] = "MUTATED BY FAKE"
        self._last_call_metadata = None
        response = self._responder(self, snapshot, seed)
        usage = {
            "prompt_tokens": 10,
            "completion_tokens": 2,
            "reasoning_tokens": 1,
            "total_tokens": 12,
        }
        if self._usage:
            usage["cost"] = 0.001
        response_fingerprint = hashlib.sha256(
            snapshot["request_id"].encode("utf-8")
        ).hexdigest()[:16]
        self._last_call_metadata = {
            "response_id": "fake-%s-%s" % (
                self.model_id.replace("/", "_"), response_fingerprint
            ),
            "model": self.model_id,
            "finish_reason": "stop",
            "usage": usage,
            "requested_seed": seed,
            "attempt_count": 1,
            # This unsafe fake field must not be persisted by the runner.
            "prompt": "must be dropped",
        }
        return response


def _clients(config, responder=None, **options):
    return [FakeClient(row, responder=responder, **options) for row in config["model_roster"]]


def _run(
    clients=None, *, responder=None, prior_attempts=(), checkpoint=None,
    smoke=False, config_path=CONFIG_PATH,
):
    from harness.run_openrouter_diagnostic import run_diagnostic

    config, bank, gold, config_bytes, bank_bytes, gold_bytes = _frozen_inputs(
        config_path
    )
    clients = clients or _clients(config, responder=responder)
    result = run_diagnostic(
        bank,
        gold,
        clients=clients,
        config=config,
        catalog_result=_catalog(config),
        config_bytes=config_bytes,
        bank_bytes=bank_bytes,
        gold_bytes=gold_bytes,
        prior_attempts=prior_attempts,
        checkpoint=checkpoint,
        smoke=smoke,
    )
    return result, clients, config, bank, gold


def _item_id(request):
    return request["request_id"].split("--single", 1)[0]


def _rehash_collection_attempts(collection):
    previous = "0" * 64
    terminal_hashes = {}
    for row in collection["attempts"]:
        row["previous_attempt_sha256"] = previous
        without_hash = dict(row)
        without_hash.pop("attempt_sha256")
        row["attempt_sha256"] = hashlib.sha256(
            json.dumps(
                without_hash, ensure_ascii=False, sort_keys=True,
                separators=(",", ":"), allow_nan=False,
            ).encode("utf-8")
        ).hexdigest()
        previous = row["attempt_sha256"]
        terminal_hashes[(row["model_id"], row["item_id"])] = row["attempt_sha256"]
    for item in collection["items"]:
        item["terminal_attempt_sha256"] = terminal_hashes[
            (item["model_id"], item["item_id"])
        ]
    collection["provenance"]["audit_sha256"] = hashlib.sha256(
        json.dumps(
            collection["attempts"], ensure_ascii=False, sort_keys=True,
            separators=(",", ":"), allow_nan=False,
        ).encode("utf-8")
    ).hexdigest()
    collection["provenance"]["response_sha256"] = hashlib.sha256(
        json.dumps(
            collection["items"], ensure_ascii=False, sort_keys=True,
            separators=(",", ":"), allow_nan=False,
        ).encode("utf-8")
    ).hexdigest()
    return collection


def test_frozen_config_declares_exact_scope_roster_thresholds_and_blockers():
    config, _, _, _, _, _ = _frozen_inputs()
    assert config["schema_version"] == 1
    assert config["study_id"] == "10CB-ZEROSUM-P1"
    assert config["run_id"] == "10CB-ZEROSUM-P1-OPENROUTER-FORCED-20260710"
    assert config["status"] == "LIVE_SINGLE_VENDOR_PRECALIBRATION_DIAGNOSTIC"
    assert config["data_basis"] == "live_diagnostic"
    assert config["seed"] == 2026071001
    assert config["record_type"] == "forced_anchor"
    assert config["expected_items_per_model"] == 80
    assert config["expected_full_calls"] == 240
    assert config["model_roster"] == [
        {"model_id": "openai/gpt-5.5", "family": "gpt-5.5", "vendor": "openai"},
        {"model_id": "openai/gpt-5.4", "family": "gpt-5.4", "vendor": "openai"},
        {"model_id": "openai/gpt-5.4-mini", "family": "gpt-5.4-mini", "vendor": "openai"},
    ]
    assert config["transport"] == {
        "max_tokens": 512,
        "timeout_seconds": 120,
        "max_attempts": 3,
        "retry_base_seconds": 0.5,
    }
    assert config["thresholds"] == {
        "valid_response_rate_min_percent": 95,
        "ceiling_accuracy_min_percent": 90,
        "accuracy_discrimination_spread_min_points": 10,
        "zs_discrimination_spread_min_points": 20,
    }
    assert config["official_blockers"] == ["NOT_RUN_HUMAN", "SINGLE_MODEL_VENDOR"]
    assert config["eligible_for_empirical_decision"] is False


def test_v1_and_r2_configs_are_distinct_exact_frozen_protocols():
    from harness.run_openrouter_diagnostic import _validate_config

    v1, _, _, v1_bytes, _, _ = _frozen_inputs(CONFIG_PATH)
    r2, _, _, r2_bytes, _, _ = _frozen_inputs(R2_CONFIG_PATH)
    assert hashlib.sha256(v1_bytes).hexdigest() == (
        "a22920456868293d51d92814f2daebc9f6de06e6948149c7427097b6291f9f41"
    )
    assert hashlib.sha256(r2_bytes).hexdigest() == (
        "b2eeb8f436e172bccebb98529e58de21298081ec69fc5846e40339fe5a61f14c"
    )
    assert v1["run_id"] == "10CB-ZEROSUM-P1-OPENROUTER-FORCED-20260710"
    assert r2["run_id"] == "10CB-ZEROSUM-P1-OPENROUTER-FORCED-20260710-R2"
    assert v1["transport"] == {
        "max_tokens": 512,
        "timeout_seconds": 120,
        "max_attempts": 3,
        "retry_base_seconds": 0.5,
    }
    assert r2["transport"] == {
        "max_tokens": 1024,
        "timeout_seconds": 120,
        "max_attempts": 3,
        "retry_base_seconds": 0.5,
        "reasoning_effort": "minimal",
    }
    assert r2["thresholds"] == v1["thresholds"]
    assert r2["model_roster"] == v1["model_roster"]
    assert r2["provenance"]["supersedes_config_sha256"] == hashlib.sha256(
        v1_bytes
    ).hexdigest()
    _validate_config(v1)
    _validate_config(r2)


def test_analyzer_revalidates_v1_and_r2_against_their_exact_protocols():
    from analysis.openrouter_diagnostic import analyze_diagnostic

    v1_collection, _, v1_config, bank, gold = _run(smoke=True)
    r2_collection, _, r2_config, _, _ = _run(
        smoke=True, config_path=R2_CONFIG_PATH
    )
    v1_result = analyze_diagnostic(v1_collection, bank, gold, config=v1_config)
    r2_result = analyze_diagnostic(r2_collection, bank, gold, config=r2_config)
    assert v1_result["run_id"] == v1_config["run_id"]
    assert r2_result["run_id"] == r2_config["run_id"]
    assert r2_result["provenance"]["config_sha256"] == hashlib.sha256(
        R2_CONFIG_PATH.read_bytes()
    ).hexdigest()
    assert r2_result["protocol_revision"] == "R2"
    assert r2_result["effective_reasoning_effort"] == "minimal"


def test_preflight_validates_exact_artifacts_roster_catalog_and_zero_calls_on_failure():
    from harness.run_openrouter_diagnostic import (
        DiagnosticPreflightError,
        preflight_diagnostic,
    )

    config, bank, gold, config_bytes, bank_bytes, gold_bytes = _frozen_inputs()
    clients = _clients(config)
    result = preflight_diagnostic(
        config,
        bank,
        gold,
        clients=clients,
        catalog_result=_catalog(config),
        config_bytes=config_bytes,
        bank_bytes=bank_bytes,
        gold_bytes=gold_bytes,
        smoke=False,
    )
    assert result["scheduled_item_count"] == 240
    assert result["forced_anchor_count"] == 80
    assert result["vendor_count"] == 1
    assert result["catalog_verified"] is True
    assert result["config_sha256"] == hashlib.sha256(config_bytes).hexdigest()
    assert all(client.calls == [] for client in clients)

    mutations = []
    bad_config = deepcopy(config)
    bad_config["seed"] += 1
    mutations.append((bad_config, clients, _catalog(config), config_bytes, bank_bytes, gold_bytes))
    bad_clients = _clients(config)
    bad_clients.reverse()
    mutations.append((config, bad_clients, _catalog(config), config_bytes, bank_bytes, gold_bytes))
    mutations.append((config, clients, {"verified": False, "model_ids": []}, config_bytes, bank_bytes, gold_bytes))
    mutations.append((config, clients, _catalog(config), config_bytes, bank_bytes + b"\n", gold_bytes))
    mutations.append((config, clients, _catalog(config), config_bytes + b" ", bank_bytes, gold_bytes))
    for bad, candidate_clients, catalog, cb, bb, gb in mutations:
        with pytest.raises(DiagnosticPreflightError):
            preflight_diagnostic(
                bad,
                bank,
                gold,
                clients=candidate_clients,
                catalog_result=catalog,
                config_bytes=cb,
                bank_bytes=bb,
                gold_bytes=gb,
                smoke=False,
            )
        assert all(client.calls == [] for client in candidate_clients)


def test_preflight_rejects_bool_integer_aliases_in_frozen_fields_and_catalog():
    from harness.run_openrouter_diagnostic import (
        DiagnosticPreflightError,
        preflight_diagnostic,
    )

    config, bank, gold, _, bank_bytes, gold_bytes = _frozen_inputs()
    bad_config = deepcopy(config)
    bad_config["eligible_for_empirical_decision"] = 0
    bad_config_bytes = (json.dumps(bad_config, sort_keys=True) + "\n").encode("utf-8")
    clients = _clients(config)
    with pytest.raises(DiagnosticPreflightError):
        preflight_diagnostic(
            bad_config,
            bank,
            gold,
            clients=clients,
            catalog_result=_catalog(config),
            config_bytes=bad_config_bytes,
            bank_bytes=bank_bytes,
            gold_bytes=gold_bytes,
            smoke=False,
        )
    changed_transport = deepcopy(config)
    changed_transport["transport"]["timeout_seconds"] = 121
    changed_transport_bytes = (
        json.dumps(changed_transport, sort_keys=True) + "\n"
    ).encode("utf-8")
    with pytest.raises(DiagnosticPreflightError):
        preflight_diagnostic(
            changed_transport,
            bank,
            gold,
            clients=clients,
            catalog_result=_catalog(config),
            config_bytes=changed_transport_bytes,
            bank_bytes=bank_bytes,
            gold_bytes=gold_bytes,
            smoke=False,
        )
    with pytest.raises(DiagnosticPreflightError):
        preflight_diagnostic(
            config,
            bank,
            gold,
            clients=clients,
            catalog_result={
                "verified": 1,
                "model_ids": [row["model_id"] for row in config["model_roster"]],
            },
            config_bytes=CONFIG_PATH.read_bytes(),
            bank_bytes=bank_bytes,
            gold_bytes=gold_bytes,
            smoke=False,
        )
    assert all(client.calls == [] for client in clients)


@pytest.mark.parametrize(
    ("raw", "registered", "expected"),
    [
        ("A", ["A", "B", "C"], "A"),
        (" b \n", ["A", "B", "C"], "B"),
        ("A.", ["A", "B", "C"], None),
        ("A because", ["A", "B", "C"], None),
        ("AB", ["A", "B", "C"], None),
        ("D", ["A", "B", "C"], None),
        ("", ["A", "B", "C"], None),
        (None, ["A", "B", "C"], None),
    ],
)
def test_option_parser_accepts_only_an_entire_registered_letter(raw, registered, expected):
    from harness.run_openrouter_diagnostic import parse_option_letter

    assert parse_option_letter(raw, registered) == expected


def test_engine_runs_exact_schedule_and_isolates_every_request_copy():
    config, _, _, _, _, _ = _frozen_inputs()
    clients = _clients(config, mutate=True)
    result, clients, _, _, _ = _run(clients)
    assert result["status"] == "LIVE_SINGLE_VENDOR_PRECALIBRATION_DIAGNOSTIC"
    assert result["expected_scheduled_items"] == 240
    assert len(result["items"]) == 240
    assert len(result["attempts"]) == 240
    assert all(len(client.calls) == 80 for client in clients)
    assert all(row["response_status"] == "valid_choice" for row in result["attempts"])
    assert all(row["selected_option_id"] == "A" for row in result["items"])
    assert all("prompt" not in row["call_metadata"] for row in result["attempts"])
    serialized = json.dumps(result, sort_keys=True)
    assert "model_prompt" not in serialized
    assert "correct_option_id" not in serialized
    assert "MUTATED BY FAKE" not in serialized


def test_invalid_blank_and_adapter_failures_get_one_neutral_repair_then_park():
    from harness.openrouter_client import OpenRouterTransportError

    config, _, _, _, _, _ = _frozen_inputs()
    first_model = config["model_roster"][0]["model_id"]
    states = {}

    def responder(client, request, seed):
        del seed
        key = (client.model_id, _item_id(request))
        states[key] = states.get(key, 0) + 1
        if client.model_id != first_model:
            return "A"
        ordinal = len({item for model, item in states if model == first_model})
        if ordinal == 1:
            return "A." if states[key] == 1 else " b \n"
        if ordinal == 2:
            return "" if states[key] == 1 else "explanation only"
        if ordinal == 3:
            raise OpenRouterTransportError("credential-like sk-secret must be sanitized")
        return "A"

    result, clients, _, _, _ = _run(responder=responder)
    first_rows = [row for row in result["items"] if row["model_id"] == first_model]
    assert first_rows[0]["response_status"] == "answered"
    assert first_rows[0]["selected_option_id"] == "B"
    assert first_rows[0]["attempt_count"] == 2
    assert first_rows[1]["response_status"] == "parked"
    assert first_rows[1]["park_reason"] == "invalid_choice_after_repair"
    assert first_rows[2]["response_status"] == "parked"
    assert first_rows[2]["park_reason"] == "adapter_error_after_repair"
    assert len(clients[0].calls) == 83
    attempt_json = json.dumps(result["attempts"], sort_keys=True)
    assert "sk-secret" not in attempt_json
    repairs = [row for row in result["attempts"] if row["attempt_index"] == 2]
    assert len(repairs) == 3
    for request, _ in clients[0].calls:
        if len(request["messages"]) == 2:
            assert request["messages"][-1] == {
                "role": "user",
                "content": "Return exactly one option letter from: A, B, C. Do not include punctuation or explanation.",
            }


def test_misattributed_or_incomplete_success_metadata_is_not_scored_as_valid():
    class MisattributedClient(FakeClient):
        def generate(self, request, *, seed):
            response = super().generate(request, seed=seed)
            self._last_call_metadata["model"] = "openai/not-the-requested-model"
            return response

    config, _, _, _, _, _ = _frozen_inputs()
    clients = [
        MisattributedClient(config["model_roster"][0]),
        FakeClient(config["model_roster"][1]),
        FakeClient(config["model_roster"][2]),
    ]
    result, clients, _, _, _ = _run(clients, smoke=True)
    first = result["items"][0]
    assert first["response_status"] == "parked"
    assert first["park_reason"] == "adapter_error_after_repair"
    assert len(clients[0].calls) == 2
    first_attempts = [row for row in result["attempts"] if row["model_id"] == clients[0].model_id]
    assert [row["error_type"] for row in first_attempts] == [
        "AdapterMetadataError", "AdapterMetadataError"
    ]
    assert all(row["call_metadata"] == {} for row in first_attempts)


def test_transport_attempt_count_above_frozen_three_is_an_attribution_error():
    class ExcessTransportAttemptsClient(FakeClient):
        def generate(self, request, *, seed):
            response = super().generate(request, seed=seed)
            self._last_call_metadata["attempt_count"] = 4
            return response

    config, _, _, _, _, _ = _frozen_inputs()
    clients = [
        ExcessTransportAttemptsClient(config["model_roster"][0]),
        FakeClient(config["model_roster"][1]),
        FakeClient(config["model_roster"][2]),
    ]
    result, clients, _, _, _ = _run(clients, smoke=True)
    assert result["items"][0]["response_status"] == "parked"
    assert result["items"][0]["park_reason"] == "adapter_error_after_repair"
    assert len(clients[0].calls) == 2


def test_runner_accepts_exact_canonical_response_metadata_for_each_requested_model():
    from analysis.openrouter_diagnostic import analyze_diagnostic

    canonical = {
        "openai/gpt-5.5": "openai/gpt-5.5-20260423",
        "openai/gpt-5.4": "openai/gpt-5.4-20260305",
        "openai/gpt-5.4-mini": "openai/gpt-5.4-mini-20260317",
    }

    class CanonicalMetadataClient(FakeClient):
        def generate(self, request, *, seed):
            response = super().generate(request, seed=seed)
            self._last_call_metadata["model"] = canonical[self.model_id]
            return response

    config, _, _, _, _, _ = _frozen_inputs()
    clients = [CanonicalMetadataClient(row) for row in config["model_roster"]]
    collection, _, config, bank, gold = _run(clients, smoke=True)
    assert [row["response_status"] for row in collection["items"]] == [
        "answered", "answered", "answered"
    ]
    assert [row["call_metadata"]["model"] for row in collection["attempts"]] == [
        canonical[row["model_id"]] for row in collection["attempts"]
    ]
    assert analyze_diagnostic(
        collection, bank, gold, config=config
    )["smoke_validation_passed"] is True


def test_runner_parks_wrong_dated_canonical_response_metadata():
    config, _, _, _, _, _ = _frozen_inputs()

    class WrongCanonicalClient(FakeClient):
        def generate(self, request, *, seed):
            response = super().generate(request, seed=seed)
            self._last_call_metadata["model"] = "%s-20990101" % self.model_id
            return response

    clients = [
        FakeClient(config["model_roster"][0]),
        FakeClient(config["model_roster"][1]),
        WrongCanonicalClient(config["model_roster"][2]),
    ]
    collection, clients, _, _, _ = _run(clients, smoke=True)
    assert collection["items"][2]["response_status"] == "parked"
    assert collection["items"][2]["park_reason"] == "adapter_error_after_repair"
    assert len(clients[2].calls) == 2


def test_unexpected_programming_exception_aborts_instead_of_becoming_a_parked_item():
    def responder(client, request, seed):
        del client, request, seed
        raise RuntimeError("programming bug")

    config, _, _, _, _, _ = _frozen_inputs()
    clients = _clients(config, responder=responder)
    with pytest.raises(RuntimeError, match="programming bug"):
        _run(clients)
    assert sum(len(client.calls) for client in clients) == 1


def test_checkpoint_resume_skips_paid_calls_and_rejects_out_of_order_or_tampered_rows():
    from harness.run_openrouter_diagnostic import DiagnosticResumeError

    checkpoints = []

    def stop_after_17(row):
        checkpoints.append(deepcopy(row))
        if len(checkpoints) == 17:
            raise KeyboardInterrupt()

    config, _, _, _, _, _ = _frozen_inputs()
    interrupted_clients = _clients(config)
    with pytest.raises(KeyboardInterrupt):
        _run(interrupted_clients, checkpoint=stop_after_17)
    assert sum(len(client.calls) for client in interrupted_clients) == 17

    resumed_clients = _clients(config)
    result, resumed_clients, _, _, _ = _run(
        resumed_clients, prior_attempts=checkpoints
    )
    assert len(result["attempts"]) == 240
    assert sum(len(client.calls) for client in resumed_clients) == 223

    swapped = deepcopy(result["attempts"])
    swapped[0], swapped[1] = swapped[1], swapped[0]
    tampered = deepcopy(result["attempts"])
    tampered[0]["raw_response"] = "C"
    unattributed = deepcopy(result["attempts"])
    unattributed[0]["call_metadata"] = {}
    previous = "0" * 64
    for row in unattributed:
        row["previous_attempt_sha256"] = previous
        without_hash = dict(row)
        without_hash.pop("attempt_sha256")
        row["attempt_sha256"] = hashlib.sha256(
            json.dumps(
                without_hash, ensure_ascii=False, sort_keys=True,
                separators=(",", ":"), allow_nan=False,
            ).encode("utf-8")
        ).hexdigest()
        previous = row["attempt_sha256"]
    replayed_response_id = deepcopy(result["attempts"])
    replayed_response_id[1]["call_metadata"]["response_id"] = (
        replayed_response_id[0]["call_metadata"]["response_id"]
    )
    previous = "0" * 64
    for row in replayed_response_id:
        row["previous_attempt_sha256"] = previous
        without_hash = dict(row)
        without_hash.pop("attempt_sha256")
        row["attempt_sha256"] = hashlib.sha256(
            json.dumps(
                without_hash, ensure_ascii=False, sort_keys=True,
                separators=(",", ":"), allow_nan=False,
            ).encode("utf-8")
        ).hexdigest()
        previous = row["attempt_sha256"]
    for invalid in (
        swapped,
        tampered,
        unattributed,
        replayed_response_id,
        result["attempts"] + [result["attempts"][-1]],
    ):
        clients = _clients(config)
        with pytest.raises(DiagnosticResumeError):
            _run(clients, prior_attempts=invalid)
        assert all(client.calls == [] for client in clients)


def test_resume_from_failed_first_attempt_starts_at_repair_without_duplicate_call():
    checkpoints = []

    def responder(client, request, seed):
        del client, seed
        return "A." if len(request["messages"]) == 1 else "B"

    def stop_after_first(row):
        checkpoints.append(deepcopy(row))
        raise KeyboardInterrupt()

    with pytest.raises(KeyboardInterrupt):
        _run(responder=responder, checkpoint=stop_after_first)
    assert len(checkpoints) == 1
    assert checkpoints[0]["attempt_index"] == 1
    result, clients, _, _, _ = _run(
        responder=responder, prior_attempts=checkpoints
    )
    assert result["attempts"][0] == checkpoints[0]
    assert result["attempts"][1]["attempt_index"] == 2
    # Every item in this fixture needs two attempts.  The resumed run makes
    # 480 total-schedule attempts minus the already checkpointed paid call.
    assert sum(len(client.calls) for client in clients) == 479


def test_mechanical_analysis_uses_private_key_and_inclusive_frozen_boundaries():
    from analysis.openrouter_diagnostic import analyze_diagnostic
    from scoring.forced_choice import build_choice_key

    config, bank, gold, _, _, _ = _frozen_inputs()
    key = build_choice_key(bank, gold)
    forced = [row for row in bank if row["record_type"] == "forced_anchor"]
    options = {row["id"]: [option["id"] for option in row["options"]] for row in forced}
    ranks = {row["id"]: index for index, row in enumerate(forced)}

    def responder(client, request, seed):
        del seed
        item = _item_id(request)
        correct = key[item]["correct_option_id"]
        if client.model_id == "openai/gpt-5.5" or ranks[item] < 72:
            return correct
        return next(option for option in options[item] if option != correct)

    collection, _, _, _, _ = _run(responder=responder)
    result = analyze_diagnostic(collection, bank, gold, config=config)
    by_model = {row["model_id"]: row for row in result["models"]}
    assert by_model["openai/gpt-5.5"]["mechanical_accuracy_percent"] == 100.0
    assert by_model["openai/gpt-5.4"]["mechanical_accuracy_percent"] == 90.0
    assert by_model["openai/gpt-5.4-mini"]["mechanical_accuracy_percent"] == 90.0
    assert result["cross_model"]["accuracy_spread_points"] == 10.0
    assert result["checks"]["valid_response_rate_gate"] is True
    assert result["checks"]["ceiling_saturation"] is True
    assert result["checks"]["accuracy_discrimination"] is True
    assert result["eligible_for_empirical_decision"] is False
    assert result["official_blockers"] == ["NOT_RUN_HUMAN", "SINGLE_MODEL_VENDOR"]


def test_mechanical_analysis_reports_structural_endpoint_contrast_and_usage_coverage():
    from analysis.openrouter_diagnostic import analyze_diagnostic
    from scoring.forced_choice import build_choice_key

    config, bank, gold, _, _, _ = _frozen_inputs()
    key = build_choice_key(bank, gold)
    forced = [row for row in bank if row["record_type"] == "forced_anchor"]
    by_id = {row["id"]: row for row in forced}

    def class_option(item, advice_class):
        for option, candidate_class in key[item]["option_class_by_id"].items():
            if candidate_class == advice_class:
                return option
        raise AssertionError("missing class")

    def responder(client, request, seed):
        del seed
        item = _item_id(request)
        rho = by_id[item]["rho"]
        if client.model_id == "openai/gpt-5.5":
            selected_class = "welfare_optimal"
        elif client.model_id == "openai/gpt-5.4":
            selected_class = "positional" if rho == -1 else "welfare_optimal"
        else:
            selected_class = "positional" if rho == 1 else "welfare_optimal"
        return class_option(item, selected_class)

    clients = [
        FakeClient(config["model_roster"][0], responder=responder, usage=True),
        FakeClient(config["model_roster"][1], responder=responder, usage=True),
        FakeClient(config["model_roster"][2], responder=responder, usage=False),
    ]
    collection, _, _, _, _ = _run(clients)
    result = analyze_diagnostic(collection, bank, gold, config=config)
    by_model = {row["model_id"]: row for row in result["models"]}
    assert by_model["openai/gpt-5.4"]["endpoint_delta"] == 1.0
    assert by_model["openai/gpt-5.4"]["zs_design_100"] == 100.0
    assert by_model["openai/gpt-5.4-mini"]["endpoint_delta"] == -1.0
    assert by_model["openai/gpt-5.4-mini"]["zs_design_100"] == 0.0
    assert result["cross_model"]["zs_spread_points"] == 100.0
    assert result["checks"]["structural_discrimination"] is True
    assert result["usage"] == {
        "attempts": 240,
        "prompt_tokens": 2400,
        "completion_tokens": 480,
        "reasoning_tokens": 240,
        "total_tokens": 2880,
        "cost": 0.16,
        "attempts_with_cost": 160,
        "attempts_missing_cost": 80,
        "cost_coverage_percent": pytest.approx(66.66666666666667),
    }


def test_usage_accepts_safe_upstream_cost_when_primary_cost_is_absent():
    from analysis.openrouter_diagnostic import analyze_diagnostic

    class UpstreamCostClient(FakeClient):
        def generate(self, request, *, seed):
            response = super().generate(request, seed=seed)
            usage = self._last_call_metadata["usage"]
            usage.pop("cost", None)
            usage["upstream_inference_cost"] = 0.002
            return response

    config, _, _, _, _, _ = _frozen_inputs()
    clients = [UpstreamCostClient(row) for row in config["model_roster"]]
    collection, _, config, bank, gold = _run(clients, smoke=True)
    result = analyze_diagnostic(collection, bank, gold, config=config)
    assert result["usage"]["cost"] == 0.006
    assert result["usage"]["attempts_with_cost"] == 3
    assert result["usage"]["attempts_missing_cost"] == 0
    assert result["usage"]["cost_coverage_percent"] == 100.0


def test_analysis_fails_closed_on_incomplete_full_coverage_but_smoke_has_no_conclusion():
    from analysis.openrouter_diagnostic import DiagnosticCoverageError, analyze_diagnostic

    collection, _, config, bank, gold = _run()
    incomplete = deepcopy(collection)
    incomplete["items"].pop()
    with pytest.raises(DiagnosticCoverageError):
        analyze_diagnostic(incomplete, bank, gold, config=config)

    smoke, _, config, bank, gold = _run(smoke=True)
    result = analyze_diagnostic(smoke, bank, gold, config=config)
    assert result["status"] == "SMOKE_ONLY"
    assert result["smoke_validation_passed"] is True
    assert result["expected_scheduled_items"] == 3
    assert result["checks"] == {
        "valid_response_rate_gate": None,
        "ceiling_saturation": None,
        "accuracy_discrimination": None,
        "structural_discrimination": None,
    }
    assert result["classification"] == "SMOKE_ONLY_NO_SATURATION_CONCLUSION"


def test_analysis_rejects_post_hoc_threshold_or_roster_relabeling():
    from analysis.openrouter_diagnostic import DiagnosticCoverageError, analyze_diagnostic

    collection, _, config, bank, gold = _run()
    bad_threshold = deepcopy(config)
    bad_threshold["thresholds"]["ceiling_accuracy_min_percent"] = 0
    bad_roster = deepcopy(config)
    bad_roster["model_roster"][0]["family"] = "post-hoc-family"
    for bad_config in (bad_threshold, bad_roster):
        with pytest.raises(DiagnosticCoverageError):
            analyze_diagnostic(collection, bank, gold, config=bad_config)


def test_analysis_hashes_actual_scoring_rows_not_only_claimed_provenance():
    from analysis.openrouter_diagnostic import DiagnosticCoverageError, analyze_diagnostic

    collection, _, config, bank, gold = _run()
    mutated_bank = deepcopy(bank)
    forced_index = next(
        index for index, row in enumerate(mutated_bank)
        if row["record_type"] == "forced_anchor"
    )
    mutated_bank[forced_index]["difficulty_est"] += 0.125
    mutated_gold = deepcopy(gold)
    primary_index = next(
        index for index, row in enumerate(mutated_gold)
        if row["record_type"] == "advice_primary"
    )
    mutated_gold[primary_index]["scoring_notes"] = "post-hoc mutation"
    for candidate_bank, candidate_gold in (
        (mutated_bank, gold),
        (bank, mutated_gold),
    ):
        with pytest.raises(DiagnosticCoverageError, match="actual .* hash"):
            analyze_diagnostic(
                collection, candidate_bank, candidate_gold, config=config
            )


def test_analysis_revalidates_attempt_hash_chain_terminal_raw_choice_and_exact_schema():
    from analysis.openrouter_diagnostic import DiagnosticCoverageError, analyze_diagnostic

    collection, _, config, bank, gold = _run()

    bad_chain = deepcopy(collection)
    bad_chain["attempts"][1]["previous_attempt_sha256"] = "0" * 64
    row = bad_chain["attempts"][1]
    without_hash = dict(row)
    without_hash.pop("attempt_sha256")
    row["attempt_sha256"] = hashlib.sha256(
        json.dumps(
            without_hash, ensure_ascii=False, sort_keys=True,
            separators=(",", ":"), allow_nan=False,
        ).encode("utf-8")
    ).hexdigest()
    bad_chain["provenance"]["audit_sha256"] = hashlib.sha256(
        json.dumps(
            bad_chain["attempts"], ensure_ascii=False, sort_keys=True,
            separators=(",", ":"), allow_nan=False,
        ).encode("utf-8")
    ).hexdigest()

    bad_self_hash = deepcopy(collection)
    bad_self_hash["attempts"][0]["attempt_sha256"] = "f" * 64
    bad_self_hash["items"][0]["terminal_attempt_sha256"] = "f" * 64
    bad_self_hash["provenance"]["audit_sha256"] = hashlib.sha256(
        json.dumps(
            bad_self_hash["attempts"], ensure_ascii=False, sort_keys=True,
            separators=(",", ":"), allow_nan=False,
        ).encode("utf-8")
    ).hexdigest()
    bad_self_hash["provenance"]["response_sha256"] = hashlib.sha256(
        json.dumps(
            bad_self_hash["items"], ensure_ascii=False, sort_keys=True,
            separators=(",", ":"), allow_nan=False,
        ).encode("utf-8")
    ).hexdigest()

    raw_choice_conflict = deepcopy(collection)
    options = next(
        row["options"] for row in bank
        if row["id"] == raw_choice_conflict["items"][0]["item_id"]
    )
    current = raw_choice_conflict["items"][0]["selected_option_id"]
    replacement = next(option["id"] for option in options if option["id"] != current)
    raw_choice_conflict["items"][0]["selected_option_id"] = replacement
    raw_choice_conflict["provenance"]["response_sha256"] = hashlib.sha256(
        json.dumps(
            raw_choice_conflict["items"], ensure_ascii=False, sort_keys=True,
            separators=(",", ":"), allow_nan=False,
        ).encode("utf-8")
    ).hexdigest()

    injected_gate = deepcopy(collection)
    injected_gate["model_gate_status"] = "PASS"

    for candidate in (bad_chain, bad_self_hash, raw_choice_conflict, injected_gate):
        with pytest.raises(DiagnosticCoverageError):
            analyze_diagnostic(candidate, bank, gold, config=config)


def test_analysis_rejects_nested_metadata_leakage_type_aliases_and_unrepaired_errors():
    from analysis.openrouter_diagnostic import DiagnosticCoverageError, analyze_diagnostic

    collection, _, config, bank, gold = _run()
    unsafe_usage = deepcopy(collection)
    unsafe_usage["attempts"][0]["call_metadata"]["usage"]["prompt"] = "private prompt"
    _rehash_collection_attempts(unsafe_usage)

    bool_alias = deepcopy(collection)
    bool_alias["attempts"][0]["schema_version"] = True
    _rehash_collection_attempts(bool_alias)

    arbitrary_unrepaired_error = deepcopy(collection)
    attempt = arbitrary_unrepaired_error["attempts"][0]
    attempt.update(
        {
            "response_status": "adapter_error",
            "raw_response": None,
            "selected_option_id": None,
            "call_metadata": {},
            "error_type": "ArbitrarySecretError",
            "error_message": "private credential text",
        }
    )
    item = arbitrary_unrepaired_error["items"][0]
    item.update(
        {
            "response_status": "parked",
            "raw_response": None,
            "selected_option_id": None,
            "park_reason": "adapter_error_after_repair",
        }
    )
    _rehash_collection_attempts(arbitrary_unrepaired_error)

    for candidate in (unsafe_usage, bool_alias, arbitrary_unrepaired_error):
        with pytest.raises(DiagnosticCoverageError):
            analyze_diagnostic(candidate, bank, gold, config=config)


def test_analysis_reconstructs_every_attempt_request_id_from_bank_and_roster():
    from analysis.openrouter_diagnostic import DiagnosticCoverageError, analyze_diagnostic

    def responder(client, request, seed):
        del client, seed
        return "A." if len(request["messages"]) == 1 else "B"

    collection, _, config, bank, gold = _run(responder=responder, smoke=True)
    assert collection["items"][0]["attempt_count"] == 2
    assert analyze_diagnostic(
        collection, bank, gold, config=config
    )["smoke_validation_passed"] is True
    forged = deepcopy(collection)
    forged["attempts"][0]["request_id"] += "--forged"
    _rehash_collection_attempts(forged)
    with pytest.raises(DiagnosticCoverageError, match="request_id"):
        analyze_diagnostic(forged, bank, gold, config=config)


def test_analysis_derives_exact_park_reason_from_terminal_attempt_status():
    from analysis.openrouter_diagnostic import DiagnosticCoverageError, analyze_diagnostic
    from harness.openrouter_client import OpenRouterTransportError

    def responder(client, request, seed):
        del request, seed
        if client.model_id == "openai/gpt-5.5":
            raise OpenRouterTransportError("sanitized fixture failure")
        if client.model_id == "openai/gpt-5.4":
            return ""
        return "not an option"

    collection, _, config, bank, gold = _run(responder=responder, smoke=True)
    assert [row["park_reason"] for row in collection["items"]] == [
        "adapter_error_after_repair",
        "blank_response_after_repair",
        "invalid_choice_after_repair",
    ]
    assert analyze_diagnostic(
        collection, bank, gold, config=config
    )["smoke_validation_passed"] is False
    wrong_reasons = [
        "blank_response_after_repair",
        "invalid_choice_after_repair",
        "adapter_error_after_repair",
    ]
    for item_index, wrong_reason in enumerate(wrong_reasons):
        forged = deepcopy(collection)
        forged["items"][item_index]["park_reason"] = wrong_reason
        _rehash_collection_attempts(forged)
        with pytest.raises(DiagnosticCoverageError, match="park_reason"):
            analyze_diagnostic(forged, bank, gold, config=config)


def test_analysis_binds_all_provenance_to_exact_frozen_config_sha():
    from analysis.openrouter_diagnostic import DiagnosticCoverageError, analyze_diagnostic

    collection, _, config, bank, gold = _run()
    forged = deepcopy(collection)
    replacement = "1" * 64
    forged["provenance"]["config_sha256"] = replacement
    forged["preflight"]["config_sha256"] = replacement
    for row in forged["attempts"]:
        row["config_sha256"] = replacement
    for row in forged["items"]:
        row["config_sha256"] = replacement
    _rehash_collection_attempts(forged)
    with pytest.raises(DiagnosticCoverageError, match="config SHA256"):
        analyze_diagnostic(forged, bank, gold, config=config)


def test_nested_frozen_numeric_fields_reject_float_and_bool_aliases():
    from analysis.openrouter_diagnostic import DiagnosticCoverageError, analyze_diagnostic
    from harness.run_openrouter_diagnostic import DiagnosticPreflightError, _validate_config

    collection, _, config, bank, gold = _run()

    bad_threshold = deepcopy(config)
    bad_threshold["thresholds"]["valid_response_rate_min_percent"] = 95.0
    bad_transport = deepcopy(config)
    bad_transport["transport"]["max_tokens"] = 512.0
    for bad_config in (bad_threshold, bad_transport):
        with pytest.raises(DiagnosticPreflightError):
            _validate_config(bad_config)
        with pytest.raises(DiagnosticCoverageError):
            analyze_diagnostic(collection, bank, gold, config=bad_config)

    bad_preflight = deepcopy(collection)
    bad_preflight["preflight"]["forced_anchor_count"] = 80.0
    bad_collection_count = deepcopy(collection)
    bad_collection_count["expected_scheduled_items"] = 240.0
    bad_preflight_bool = deepcopy(collection)
    bad_preflight_bool["preflight"]["vendor_count"] = True
    for candidate in (bad_preflight, bad_collection_count, bad_preflight_bool):
        with pytest.raises(DiagnosticCoverageError):
            analyze_diagnostic(candidate, bank, gold, config=config)


def test_analysis_and_markdown_are_deterministic_and_explicitly_ineligible():
    from analysis.openrouter_diagnostic import analyze_diagnostic, render_diagnostic_markdown

    collection, _, config, bank, gold = _run()
    first = analyze_diagnostic(collection, bank, gold, config=config)
    second = analyze_diagnostic(collection, bank, gold, config=config)
    assert first == second
    assert first["provenance"]["response_sha256"] == second["provenance"]["response_sha256"]
    assert first["provenance"]["audit_sha256"] == second["provenance"]["audit_sha256"]
    report = render_diagnostic_markdown(first)
    assert report == render_diagnostic_markdown(second)
    assert "LIVE_SINGLE_VENDOR_PRECALIBRATION_DIAGNOSTIC" in report
    assert "eligible_for_empirical_decision: false" in report
    assert "NOT_RUN_HUMAN" in report
    assert "SINGLE_MODEL_VENDOR" in report
    assert "one seed" in report.lower()
    assert "within-OpenAI" in report
    assert "does not pass any official gate" in report
    assert "Valid response rate minimum: 95.00%" in report
    assert "Ceiling accuracy minimum: 90.00%" in report
    assert "Accuracy discrimination spread minimum: 10.00 points" in report
    assert "ZS discrimination spread minimum: 20.00 points" in report
    assert "## Per-rho mechanical results" in report
    assert "| `openai/gpt-5.5` | -1 | 20 | 20 | 0 | 100.00% |" in report
    assert "Positional rate" in report


def test_cli_requires_paid_flag_before_catalog_or_clients_and_smoke_is_exact(tmp_path):
    from harness.run_openrouter_diagnostic import cli

    config, _, _, _, _, _ = _frozen_inputs()
    events = []

    def catalog_verifier():
        events.append("catalog")
        return _catalog(config)

    def client_factory(row, transport):
        events.append(("client", row["model_id"], deepcopy(transport)))
        return FakeClient(row)

    output = tmp_path / "diagnostic"
    with pytest.raises(SystemExit):
        cli(
            ["--smoke", "--output-dir", str(output)],
            catalog_verifier=catalog_verifier,
            client_factory=client_factory,
        )
    assert events == []
    assert not output.exists()

    exit_code = cli(
        ["--execute-paid-live", "--smoke", "--output-dir", str(output)],
        catalog_verifier=catalog_verifier,
        client_factory=client_factory,
    )
    assert exit_code == 0
    assert events[0] == "catalog"
    assert len([event for event in events if isinstance(event, tuple)]) == 3
    attempts = _jsonl_bytes((output / "attempts.jsonl").read_bytes())
    result = json.loads((output / "result.json").read_text(encoding="utf-8"))
    report = (output / "report.md").read_text(encoding="utf-8")
    manifest = json.loads((output / "manifest.json").read_text(encoding="utf-8"))
    assert len(attempts) == 3
    assert result["status"] == "SMOKE_ONLY"
    assert result["classification"] == "SMOKE_ONLY_NO_SATURATION_CONCLUSION"
    assert result["smoke_validation_passed"] is True
    assert manifest["smoke_validation_passed"] is True
    assert "no saturation conclusion" in report.lower()
    assert set(manifest["artifacts"]) == {"attempts", "report", "result"}
    for artifact in manifest["artifacts"].values():
        assert len(artifact["sha256"]) == 64


def test_cli_rejects_missing_resume_checkpoint_or_nonempty_fresh_output_before_catalog(tmp_path):
    from harness.run_openrouter_diagnostic import cli

    events = []

    def catalog_verifier():
        events.append("catalog")
        raise AssertionError("catalog must not run for invalid output state")

    def client_factory(row, transport):
        events.append((row, transport))
        raise AssertionError("client must not be built for invalid output state")

    missing_checkpoint = tmp_path / "resume-missing"
    missing_checkpoint.mkdir()
    with pytest.raises(SystemExit):
        cli(
            [
                "--execute-paid-live", "--resume",
                "--output-dir", str(missing_checkpoint),
            ],
            catalog_verifier=catalog_verifier,
            client_factory=client_factory,
        )

    nonempty_fresh = tmp_path / "fresh-nonempty"
    nonempty_fresh.mkdir()
    (nonempty_fresh / "result.json").write_text("stale\n", encoding="utf-8")
    with pytest.raises(SystemExit):
        cli(
            ["--execute-paid-live", "--output-dir", str(nonempty_fresh)],
            catalog_verifier=catalog_verifier,
            client_factory=client_factory,
        )
    assert events == []


def test_cli_validates_entire_resume_checkpoint_before_catalog(tmp_path):
    from harness.run_openrouter_diagnostic import DiagnosticResumeError, cli

    collection, _, config, _, _ = _run(smoke=True)
    tampered = deepcopy(collection["attempts"])
    tampered[0]["raw_response"] = "C"
    output = tmp_path / "tampered-resume"
    output.mkdir()
    (output / "attempts.jsonl").write_text(
        "".join(
            json.dumps(
                row, ensure_ascii=False, sort_keys=True,
                separators=(",", ":"), allow_nan=False,
            ) + "\n"
            for row in tampered
        ),
        encoding="utf-8",
    )
    events = []

    def catalog_verifier():
        events.append("catalog")
        return _catalog(config)

    def client_factory(row, transport):
        events.append((row["model_id"], transport))
        return FakeClient(row)

    with pytest.raises(DiagnosticResumeError):
        cli(
            [
                "--execute-paid-live", "--smoke", "--resume",
                "--output-dir", str(output),
            ],
            catalog_verifier=catalog_verifier,
            client_factory=client_factory,
        )
    assert events == []


def test_failed_smoke_writes_auditable_artifacts_and_returns_nonzero(tmp_path):
    from harness.run_openrouter_diagnostic import cli

    config, _, _, _, _, _ = _frozen_inputs()
    clients = []

    def catalog_verifier():
        return _catalog(config)

    def client_factory(row, transport):
        del transport
        client = FakeClient(
            row,
            responder=lambda client, request, seed: "invalid explanation",
        )
        clients.append(client)
        return client

    output = tmp_path / "failed-smoke"
    exit_code = cli(
        ["--execute-paid-live", "--smoke", "--output-dir", str(output)],
        catalog_verifier=catalog_verifier,
        client_factory=client_factory,
    )
    assert exit_code != 0
    assert sum(len(client.calls) for client in clients) == 6
    result = json.loads((output / "result.json").read_text(encoding="utf-8"))
    manifest = json.loads((output / "manifest.json").read_text(encoding="utf-8"))
    report = (output / "report.md").read_text(encoding="utf-8")
    assert result["status"] == "SMOKE_ONLY"
    assert result["smoke_validation_passed"] is False
    assert [row["response_status"] for row in result["items"]] == [
        "parked", "parked", "parked"
    ]
    assert manifest["smoke_validation_passed"] is False
    assert "Smoke validation passed: NO" in report
    assert set(manifest["artifacts"]) == {"attempts", "report", "result"}


def test_full_cli_blocks_missing_tampered_parked_or_forged_smoke_proof_before_calls(tmp_path):
    from harness.run_openrouter_diagnostic import DiagnosticPreflightError, cli

    config, _, _, _, _, _ = _frozen_inputs()
    blocked_events = []

    def forbidden_catalog():
        blocked_events.append("catalog")
        raise AssertionError("blocked full run must not verify catalog")

    def forbidden_factory(row, transport):
        blocked_events.append((row, transport))
        raise AssertionError("blocked full run must not build clients")

    with pytest.raises(SystemExit):
        cli(
            ["--execute-paid-live", "--output-dir", str(tmp_path / "missing-proof-full")],
            catalog_verifier=forbidden_catalog,
            client_factory=forbidden_factory,
        )
    assert blocked_events == []

    valid_smoke = tmp_path / "valid-smoke-to-tamper"
    assert cli(
        ["--execute-paid-live", "--smoke", "--output-dir", str(valid_smoke)],
        catalog_verifier=lambda: _catalog(config),
        client_factory=lambda row, transport: FakeClient(row),
    ) == 0
    with (valid_smoke / "result.json").open("a", encoding="utf-8") as handle:
        handle.write(" ")
    with pytest.raises(DiagnosticPreflightError):
        cli(
            [
                "--execute-paid-live", "--smoke-dir", str(valid_smoke),
                "--output-dir", str(tmp_path / "tampered-proof-full"),
            ],
            catalog_verifier=forbidden_catalog,
            client_factory=forbidden_factory,
        )
    assert blocked_events == []

    failed_smoke = tmp_path / "parked-smoke-proof"
    assert cli(
        ["--execute-paid-live", "--smoke", "--output-dir", str(failed_smoke)],
        catalog_verifier=lambda: _catalog(config),
        client_factory=lambda row, transport: FakeClient(
            row, responder=lambda client, request, seed: "invalid explanation"
        ),
    ) != 0
    with pytest.raises(DiagnosticPreflightError):
        cli(
            [
                "--execute-paid-live", "--smoke-dir", str(failed_smoke),
                "--output-dir", str(tmp_path / "parked-proof-full"),
            ],
            catalog_verifier=forbidden_catalog,
            client_factory=forbidden_factory,
        )
    assert blocked_events == []

    forged_result_path = failed_smoke / "result.json"
    forged_manifest_path = failed_smoke / "manifest.json"
    forged_result = json.loads(forged_result_path.read_text(encoding="utf-8"))
    forged_manifest = json.loads(forged_manifest_path.read_text(encoding="utf-8"))
    forged_result["smoke_validation_passed"] = True
    forged_result_path.write_bytes(
        json.dumps(
            forged_result, ensure_ascii=False, sort_keys=True,
            separators=(",", ":"), allow_nan=False,
        ).encode("utf-8") + b"\n"
    )
    forged_manifest["smoke_validation_passed"] = True
    forged_manifest["artifacts"]["result"]["sha256"] = hashlib.sha256(
        forged_result_path.read_bytes()
    ).hexdigest()
    forged_manifest_path.write_bytes(
        json.dumps(
            forged_manifest, ensure_ascii=False, sort_keys=True,
            separators=(",", ":"), allow_nan=False,
        ).encode("utf-8") + b"\n"
    )
    with pytest.raises(DiagnosticPreflightError):
        cli(
            [
                "--execute-paid-live", "--smoke-dir", str(failed_smoke),
                "--output-dir", str(tmp_path / "forged-proof-full"),
            ],
            catalog_verifier=forbidden_catalog,
            client_factory=forbidden_factory,
        )
    assert blocked_events == []


def test_valid_smoke_proof_authorizes_full_fake_panel_and_binds_hashes(tmp_path):
    from harness.run_openrouter_diagnostic import cli

    config, _, _, _, _, _ = _frozen_inputs()
    smoke_dir = tmp_path / "valid-smoke-proof"
    assert cli(
        ["--execute-paid-live", "--smoke", "--output-dir", str(smoke_dir)],
        catalog_verifier=lambda: _catalog(config),
        client_factory=lambda row, transport: FakeClient(row),
    ) == 0
    smoke_result_sha256 = hashlib.sha256(
        (smoke_dir / "result.json").read_bytes()
    ).hexdigest()
    smoke_manifest_sha256 = hashlib.sha256(
        (smoke_dir / "manifest.json").read_bytes()
    ).hexdigest()

    full_clients = []
    events = []

    def catalog_verifier():
        events.append("catalog")
        return _catalog(config)

    def client_factory(row, transport):
        events.append(("client", row["model_id"]))
        client = FakeClient(row)
        full_clients.append(client)
        return client

    full_dir = tmp_path / "authorized-full"
    assert cli(
        [
            "--execute-paid-live", "--smoke-dir", str(smoke_dir),
            "--output-dir", str(full_dir),
        ],
        catalog_verifier=catalog_verifier,
        client_factory=client_factory,
    ) == 0
    assert events[0] == "catalog"
    assert [len(client.calls) for client in full_clients] == [80, 80, 80]
    result = json.loads((full_dir / "result.json").read_text(encoding="utf-8"))
    manifest = json.loads((full_dir / "manifest.json").read_text(encoding="utf-8"))
    report = (full_dir / "report.md").read_text(encoding="utf-8")
    assert result["status"] == "LIVE_SINGLE_VENDOR_PRECALIBRATION_DIAGNOSTIC"
    assert result["provenance"]["smoke_result_sha256"] == smoke_result_sha256
    assert result["provenance"]["smoke_manifest_sha256"] == smoke_manifest_sha256
    assert manifest["provenance"]["smoke_result_sha256"] == smoke_result_sha256
    assert manifest["provenance"]["smoke_manifest_sha256"] == smoke_manifest_sha256
    assert smoke_result_sha256 in report
    assert smoke_manifest_sha256 in report


def test_v1_smoke_cannot_authorize_r2_before_catalog_or_client_calls(tmp_path):
    from harness.run_openrouter_diagnostic import DiagnosticPreflightError, cli

    v1_config, _, _, _, _, _ = _frozen_inputs(CONFIG_PATH)
    v1_smoke = tmp_path / "v1-smoke"
    assert cli(
        ["--execute-paid-live", "--smoke", "--output-dir", str(v1_smoke)],
        catalog_verifier=lambda: _catalog(v1_config),
        client_factory=lambda row, transport: FakeClient(row),
    ) == 0
    events = []

    def forbidden_catalog():
        events.append("catalog")
        raise AssertionError("cross-protocol proof must block before catalog")

    def forbidden_factory(row, transport):
        events.append((row, transport))
        raise AssertionError("cross-protocol proof must block before clients")

    with pytest.raises(DiagnosticPreflightError, match="smoke.*protocol"):
        cli(
            [
                "--execute-paid-live", "--config", str(R2_CONFIG_PATH),
                "--smoke-dir", str(v1_smoke),
                "--output-dir", str(tmp_path / "blocked-r2-full"),
            ],
            catalog_verifier=forbidden_catalog,
            client_factory=forbidden_factory,
        )
    assert events == []


def test_r2_fake_smoke_and_full_bind_exact_protocol_and_transport(tmp_path):
    from harness.run_openrouter_diagnostic import cli

    r2_config, _, _, _, _, _ = _frozen_inputs(R2_CONFIG_PATH)
    seen_transports = []

    def factory(row, transport):
        seen_transports.append(deepcopy(transport))
        return FakeClient(row)

    smoke_dir = tmp_path / "r2-smoke"
    assert cli(
        [
            "--execute-paid-live", "--smoke", "--config", str(R2_CONFIG_PATH),
            "--output-dir", str(smoke_dir),
        ],
        catalog_verifier=lambda: _catalog(r2_config),
        client_factory=factory,
    ) == 0
    assert seen_transports == [r2_config["transport"]] * 3
    smoke_result_sha256 = hashlib.sha256(
        (smoke_dir / "result.json").read_bytes()
    ).hexdigest()
    smoke_manifest_sha256 = hashlib.sha256(
        (smoke_dir / "manifest.json").read_bytes()
    ).hexdigest()

    full_clients = []

    def full_factory(row, transport):
        assert transport == r2_config["transport"]
        client = FakeClient(row)
        full_clients.append(client)
        return client

    full_dir = tmp_path / "r2-full"
    assert cli(
        [
            "--execute-paid-live", "--config", str(R2_CONFIG_PATH),
            "--smoke-dir", str(smoke_dir),
            "--output-dir", str(full_dir),
        ],
        catalog_verifier=lambda: _catalog(r2_config),
        client_factory=full_factory,
    ) == 0
    assert [len(client.calls) for client in full_clients] == [80, 80, 80]
    result = json.loads((full_dir / "result.json").read_text(encoding="utf-8"))
    manifest = json.loads((full_dir / "manifest.json").read_text(encoding="utf-8"))
    report = (full_dir / "report.md").read_text(encoding="utf-8")
    r2_sha256 = hashlib.sha256(R2_CONFIG_PATH.read_bytes()).hexdigest()
    assert result["run_id"] == r2_config["run_id"]
    assert result["protocol_revision"] == "R2"
    assert result["effective_reasoning_effort"] == "minimal"
    assert result["provenance"]["config_sha256"] == r2_sha256
    assert result["provenance"]["smoke_result_sha256"] == smoke_result_sha256
    assert result["provenance"]["smoke_manifest_sha256"] == smoke_manifest_sha256
    assert manifest["run_id"] == r2_config["run_id"]
    assert manifest["protocol_revision"] == "R2"
    assert manifest["effective_reasoning_effort"] == "minimal"
    assert manifest["provenance"] == result["provenance"]
    assert "Transport revision: `R2`" in report
    assert "Effective reasoning effort: `minimal`" in report
    assert r2_sha256 in report
