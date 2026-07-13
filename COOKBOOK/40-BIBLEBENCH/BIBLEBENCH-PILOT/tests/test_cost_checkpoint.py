from __future__ import annotations

from decimal import Decimal
import json
from pathlib import Path


PACKAGE_ROOT = Path(__file__).parents[1]
CHECKPOINT = PACKAGE_ROOT / "pilot-cost-estimate.json"


def test_cost_checkpoint_is_exact_recomputable_and_non_authorizing() -> None:
    data = json.loads(CHECKPOINT.read_text(encoding="utf-8"))

    assert data["status"] == "PROPOSAL_ONLY"
    assert data["authorized"] is False
    assert data["calls_made"] == 0
    assert Decimal(str(data["spend_usd"])) == Decimal("0")
    assert len(data["models"]) == 4
    assert len({route["provider_family"] for route in data["models"]}) == 4
    assert len({route["model_id"] for route in data["models"]}) == 4

    total = Decimal("0")
    caps = data["token_caps_per_model"]
    input_tokens = caps["pilot_input_tokens"] + caps["smoke_input_tokens"]
    output_tokens = caps["pilot_output_tokens"] + caps["smoke_output_tokens"]
    for route in data["models"]:
        expected = (
            Decimal(input_tokens)
            * Decimal(str(route["input_usd_per_million_tokens"]))
            + Decimal(output_tokens)
            * Decimal(str(route["output_usd_per_million_tokens"]))
        ) / Decimal("1000000")
        recorded = Decimal(str(route["route_total_worst_case_usd"]))
        assert recorded == expected
        assert all(url.startswith("https://") for url in route["official_sources"])
        total += recorded

    assert Decimal(str(data["subtotal_worst_case_usd"])) == total
    assert Decimal(str(data["contingency_fraction"])) == Decimal("0.2")
    assert Decimal(str(data["proposed_hard_nte_usd"])) == Decimal("4")
    assert any("3.60 USD" in rule for rule in data["stop_rules"])
    assert data["geometry"]["maximum_total_calls"] == 1356
