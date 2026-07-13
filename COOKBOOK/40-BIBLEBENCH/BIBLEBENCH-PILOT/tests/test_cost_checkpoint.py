from __future__ import annotations

from decimal import Decimal
import json
from pathlib import Path


PACKAGE_ROOT = Path(__file__).parents[1]
CHECKPOINT = PACKAGE_ROOT / "pilot-cost-estimate.json"


def test_cost_checkpoint_is_exact_recomputable_and_non_authorizing() -> None:
    data = json.loads(CHECKPOINT.read_text(encoding="utf-8"))
    assert data["estimate_version"] == "pf002-three-model-preflight-v1"
    assert data["status"] == "PROPOSAL_ONLY"
    assert data["authorized"] is False
    assert data["calls_made"] == 0
    assert Decimal(str(data["spend_usd"])) == Decimal("0")
    assert data["geometry"] == {
        "actors": 3,
        "episodes": 48,
        "primary_calls": 144,
        "probe_calls": 144,
        "logical_calls": 288,
        "maximum_attempts_per_logical_call": 2,
    }
    total = Decimal("0")
    for actor in data["models"]:
        expected = Decimal(192) * (
            Decimal(4096)
            * Decimal(str(actor["input_usd_per_million_tokens"]))
            + Decimal(700)
            * Decimal(str(actor["output_usd_per_million_tokens"]))
        ) / Decimal("1000000")
        assert Decimal(str(actor["route_worst_case_usd"])) == expected
        total += expected
    assert Decimal(str(data["calculated_worst_case_usd"])) == total
    assert Decimal(str(data["forecast_usd"])) == total
    assert total <= Decimal("3")
    assert Decimal(str(data["forecast_limit_usd"])) == Decimal("3")
    assert Decimal(str(data["hard_nte_usd"])) == Decimal("5")
