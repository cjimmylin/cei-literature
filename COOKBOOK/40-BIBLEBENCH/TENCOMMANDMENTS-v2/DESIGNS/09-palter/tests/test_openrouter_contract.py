from collections import Counter


def test_frozen_cheap_configs_have_exact_static_schedules_and_spend_caps():
    from harness import palter_openrouter as transport

    smoke = transport.preflight_config(transport.SMOKE_CONFIG_PATH)
    assert smoke.config_sha256 == transport.SMOKE_CONFIG_SHA256
    assert smoke.config["mode"] == "CHEAP_OPENROUTER_ENGINEERING_SMOKE"
    assert smoke.config["bt_status"] == "NOT_RUN"
    assert smoke.config["eligible_for_empirical_decision"] is False
    assert len(smoke.schedule) == 51
    assert len(smoke.preflight.calls) == 102
    assert smoke.preflight.cost_cap == transport.Decimal("0.10")
    assert smoke.preflight.cost_upper_bound == transport.Decimal("0.0191488")
    assert Counter(row.role for row in smoke.schedule) == {
        "evaluated": 15,
        "reader": 18,
        "atom_audit": 18,
    }
    assert Counter(row.route_model_id for row in smoke.schedule) == {
        "inclusionai/ling-2.6-flash": 17,
        "meta-llama/llama-3.1-8b-instruct": 17,
        "mistralai/mistral-nemo": 17,
    }
    assert smoke.routes[0].canonical_model_id == (
        "inclusionai/ling-2.6-flash-20260421"
    )

    full = transport.preflight_config(transport.FULL_CONFIG_PATH)
    assert full.config_sha256 == transport.FULL_CONFIG_SHA256
    assert full.config["mode"] == "CHEAP_OPENROUTER_FULL_DIAGNOSTIC"
    assert full.config["bt_status"] == "NOT_RUN"
    assert full.config["eligible_for_empirical_decision"] is False
    assert len(full.schedule) == 3720
    assert len(full.preflight.calls) == 7440
    assert full.preflight.cost_cap == transport.Decimal("2")
    assert full.preflight.cost_upper_bound == transport.Decimal("1.396736")
    assert Counter(row.role for row in full.schedule) == {
        "evaluated": 936,
        "reader": 1392,
        "atom_audit": 1392,
    }
    assert Counter(row.route_model_id for row in full.schedule) == {
        "inclusionai/ling-2.6-flash": 1240,
        "meta-llama/llama-3.1-8b-instruct": 1240,
        "mistralai/mistral-nemo": 1240,
    }
    assert full.routes[0].canonical_model_id == (
        "inclusionai/ling-2.6-flash-20260421"
    )
