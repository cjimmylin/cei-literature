"""Reserved agreement decisions exposed only as injected typed strategies."""
from __future__ import annotations

import math
from typing import Protocol, Sequence, TypeVar


Label = TypeVar("Label")


class ReservedMetricStrategyError(RuntimeError):
    pass


class WeightedKappaStrategy(Protocol[Label]):
    strategy_id: str

    def compute(self, left: Sequence[Label], right: Sequence[Label]) -> float:
        ...


def weighted_kappa(
    left: Sequence[Label],
    right: Sequence[Label],
    *,
    strategy: WeightedKappaStrategy[Label] = None,
) -> float:
    """Delegate κw to an explicitly frozen strategy; there is no stack default."""

    if strategy is None:
        raise ReservedMetricStrategyError(
            "κw weight/order strategy is RESERVED — inject a frozen strategy"
        )
    strategy_id = getattr(strategy, "strategy_id", None)
    if not isinstance(strategy_id, str) or not strategy_id:
        raise ReservedMetricStrategyError("weighted κ strategy requires strategy_id")
    if len(left) != len(right):
        raise ValueError("weighted κ label vectors must have equal length")
    value = strategy.compute(left, right)
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError("weighted κ strategy must return a numeric value")
    result = float(value)
    if not math.isfinite(result):
        raise ValueError("weighted κ strategy result must be finite")
    if result < -1.0 or result > 1.0:
        raise ValueError("weighted κ strategy result outside [-1, 1] range")
    return result
