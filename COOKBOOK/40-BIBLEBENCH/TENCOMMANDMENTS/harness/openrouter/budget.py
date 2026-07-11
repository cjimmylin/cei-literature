"""Exact preflight and paid-response spend custody for resumable runs."""

from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
import threading
from typing import Any, Dict, Iterable, Mapping, Optional, Sequence, Tuple


class SpendError(ValueError):
    """Base class for spend preflight and ledger failures."""


class SpendPreflightError(SpendError):
    """Raised before execution when the exact schedule is not affordable."""


class SpendLedgerError(SpendError):
    """Raised when a paid call cannot be reconciled to the frozen schedule."""


class SpendCapExceeded(SpendLedgerError):
    """Raised after an already-paid response is custodied above a bound."""


def _identifier(value: Any, label: str, error_type: type) -> str:
    if type(value) is not str or not value.strip() or value.strip() != value:
        raise error_type("%s must be nonblank exact text" % label)
    return value


def _decimal_money(
    value: Any,
    label: str,
    error_type: type,
    *,
    positive: bool = False,
) -> Decimal:
    if isinstance(value, bool) or not isinstance(value, (str, int, float, Decimal)):
        raise error_type("%s must be a finite decimal amount" % label)
    try:
        amount = Decimal(str(value))
    except (InvalidOperation, ValueError):
        raise error_type("%s must be a finite decimal amount" % label) from None
    if not amount.is_finite():
        raise error_type("%s must be finite" % label)
    if amount < 0:
        raise error_type("%s must be nonnegative" % label)
    if positive and amount == 0:
        raise error_type("%s must be positive" % label)
    return amount


def _money_text(value: Decimal) -> str:
    text = format(value, "f")
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    return "0" if text in {"", "-0"} else text


@dataclass(frozen=True)
class CallEstimate:
    """One logical paid call and its conservative maximum cost."""

    call_id: str
    max_cost_usd: Any


@dataclass(frozen=True)
class SpendPreflight:
    """Immutable proof that an exact logical-call schedule fits its cap."""

    calls: Tuple[CallEstimate, ...]
    cost_cap: Decimal
    cost_upper_bound: Decimal

    def to_dict(self) -> Dict[str, Any]:
        return {
            "schema_version": 1,
            "scheduled_call_count": len(self.calls),
            "cost_cap_usd": _money_text(self.cost_cap),
            "cost_upper_bound_usd": _money_text(self.cost_upper_bound),
            "remaining_margin_usd": _money_text(
                self.cost_cap - self.cost_upper_bound
            ),
            "calls": [
                {
                    "call_id": row.call_id,
                    "max_cost_usd": _money_text(row.max_cost_usd),
                }
                for row in self.calls
            ],
        }


def preflight_spend(
    estimates: Iterable[CallEstimate], *, cost_cap_usd: Any
) -> SpendPreflight:
    """Bind every logical call and prove its total upper bound is affordable."""

    cap = _decimal_money(
        cost_cap_usd,
        "cost_cap_usd",
        SpendPreflightError,
        positive=True,
    )
    try:
        source = tuple(estimates)
    except TypeError:
        raise SpendPreflightError("call estimates must be iterable") from None
    if not source:
        raise SpendPreflightError("call schedule must not be empty")
    normalized = []
    seen = set()
    total = Decimal("0")
    for row in source:
        if type(row) is not CallEstimate:
            raise SpendPreflightError("schedule rows must be exact CallEstimate values")
        call_id = _identifier(row.call_id, "call_id", SpendPreflightError)
        if call_id in seen:
            raise SpendPreflightError("duplicate call_id in spend schedule")
        seen.add(call_id)
        maximum = _decimal_money(
            row.max_cost_usd,
            "max_cost_usd",
            SpendPreflightError,
        )
        normalized.append(CallEstimate(call_id, maximum))
        total += maximum
    if total > cap:
        raise SpendPreflightError("schedule cost upper bound exceeds cost cap")
    return SpendPreflight(tuple(normalized), cap, total)


@dataclass(frozen=True)
class SpendRecord:
    """One paid response and the cumulative spend immediately after it."""

    call_id: str
    cost_usd: str
    cumulative_cost_usd: str

    def to_dict(self) -> Dict[str, str]:
        return {
            "call_id": self.call_id,
            "cost_usd": self.cost_usd,
            "cumulative_cost_usd": self.cumulative_cost_usd,
        }


class SpendLedger:
    """Thread-safe exact ledger that can be rebuilt from checkpoint records."""

    def __init__(
        self,
        preflight: SpendPreflight,
        *,
        prior_records: Optional[Sequence[Mapping[str, Any]]] = None,
    ) -> None:
        if type(preflight) is not SpendPreflight:
            raise SpendLedgerError("ledger requires an exact SpendPreflight")
        self._preflight = preflight
        self._limits = {row.call_id: row.max_cost_usd for row in preflight.calls}
        self._records = []  # type: list
        self._inflight = set()
        self._spent = Decimal("0")
        self._lock = threading.Lock()
        for record in tuple(prior_records or ()):
            self._restore_record(record)

    def _restore_record(self, value: Mapping[str, Any]) -> None:
        if type(value) is not dict or set(value) != {
            "call_id",
            "cost_usd",
            "cumulative_cost_usd",
        }:
            raise SpendLedgerError("prior spend record schema is invalid")
        expected_cumulative = value["cumulative_cost_usd"]
        record = self._record(value["call_id"], value["cost_usd"], restoring=True)
        normalized = _money_text(
            _decimal_money(
                expected_cumulative,
                "cumulative_cost_usd",
                SpendLedgerError,
            )
        )
        if record.cumulative_cost_usd != normalized:
            raise SpendLedgerError("prior spend record cumulative cost is invalid")

    def authorize_call(self, call_id: str) -> None:
        """Atomically reserve one scheduled, unpaid call before transport."""

        resolved = _identifier(call_id, "call_id", SpendLedgerError)
        with self._lock:
            if resolved not in self._limits:
                raise SpendLedgerError("call_id is outside the preflight schedule")
            if any(row.call_id == resolved for row in self._records):
                raise SpendLedgerError("call_id was already recorded")
            if resolved in self._inflight:
                raise SpendLedgerError("call_id is already reserved in-flight")
            self._inflight.add(resolved)

    def release_call(self, call_id: str) -> None:
        """Release a reservation only after a known uncharged failure."""

        resolved = _identifier(call_id, "call_id", SpendLedgerError)
        with self._lock:
            if resolved not in self._inflight:
                raise SpendLedgerError("call_id is not reserved in-flight")
            self._inflight.remove(resolved)

    def _record(
        self, call_id: Any, cost_usd: Any, *, restoring: bool = False
    ) -> SpendRecord:
        resolved = _identifier(call_id, "call_id", SpendLedgerError)
        if resolved not in self._limits:
            raise SpendLedgerError("call_id is outside the preflight schedule")
        if any(row.call_id == resolved for row in self._records):
            raise SpendLedgerError("call_id was already recorded")
        cost = _decimal_money(cost_usd, "cost_usd", SpendLedgerError)
        self._inflight.discard(resolved)
        self._spent += cost
        record = SpendRecord(
            resolved,
            _money_text(cost),
            _money_text(self._spent),
        )
        self._records.append(record)
        if cost > self._limits[resolved] or self._spent > self._preflight.cost_cap:
            message = "paid response exceeded its preflight spend bound"
            if restoring:
                raise SpendLedgerError(message)
            raise SpendCapExceeded(message)
        return record

    def record_paid_call(self, call_id: str, cost_usd: Any) -> SpendRecord:
        """Custody one actual response cost before reporting any bound overrun."""

        with self._lock:
            return self._record(call_id, cost_usd)

    @property
    def records(self) -> Tuple[SpendRecord, ...]:
        with self._lock:
            return tuple(self._records)

    @property
    def completed_call_ids(self) -> Tuple[str, ...]:
        with self._lock:
            return tuple(row.call_id for row in self._records)

    @property
    def inflight_call_ids(self) -> Tuple[str, ...]:
        with self._lock:
            return tuple(
                row.call_id
                for row in self._preflight.calls
                if row.call_id in self._inflight
            )

    @property
    def spent_cost_usd(self) -> str:
        with self._lock:
            return _money_text(self._spent)

    @property
    def remaining_cost_usd(self) -> str:
        with self._lock:
            return _money_text(self._preflight.cost_cap - self._spent)


__all__ = [
    "CallEstimate",
    "SpendCapExceeded",
    "SpendError",
    "SpendLedger",
    "SpendLedgerError",
    "SpendPreflight",
    "SpendPreflightError",
    "SpendRecord",
    "preflight_spend",
]
